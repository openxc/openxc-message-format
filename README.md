# OpenXC Message Format Specification

Version: v0.2

This specification is a part of the [OpenXC platform][OpenXC].

An OpenXC vehicle interface sends generic vehicle data over one or more output
interfaces (e.g. USB or Bluetooth) as JSON or Protocol Buffers (protobuf).

This document describes the JSON format and includes a high level description of
each type and field. Each JSON message published by a VI is delimited with a
`\0` character.

The Protocol Buffer format is specified in the file `openxc.proto`. Those are
published using the standard length-delimited method (any protobuf library
should support this).

## Single Valued

There may not be a 1:1 relationship between input and output signals - i.e. raw
engine timing CAN signals may be summarized in an "engine performance" metric on
the abstract side of the interface.

The expected format of a single valued message is:

    {"name": "steering_wheel_angle", "value": 45}

## Evented

The expected format of an event message is:

    {"name": "button_event", "value": "up", "event": "pressed"}

This format is good for something like a button event, where there are two
discrete pieces of information in the measurement.

## Raw CAN Message format

The format for a raw CAN message:

    {"bus": 1, "id": 1234, "value": "0x12345678"}

**bus** - the numerical identifier of the CAN bus where this message originated,
  most likely 1 or 2 (for a vehicle interface with 2 CAN controllers).

**id** - the CAN message ID

**data** - up to 8 bytes of data from the CAN message's payload, represented as
  a hexidecimal number in a string. Many JSON parser cannot handle 64-bit
  integers, which is why we are not using a numerical data type. Each byte in
  the string *must* be represented with 2 characters, e.g. `0x1` is `0x01` - the
  complete string must have an even number of characters.

## Diagnostic Messages

### Requests

A request to add or update a diagnostic request is sent to a vehicle interface
with this command format:

    { "command": "diagnostic_request",
      "request": {
          "bus": 1,
          "id": 1234,
          "mode": 1,
          "pid": 5,
          "payload": "0x1234",
          "multiple_responses": false,
          "factor": 1.0,
          "offset": 0,
          "frequency": 1,
          "name": "my_pid"
        }
      }
    }

**bus** - the numerical identifier of the CAN bus where this request should be
    sent, most likely 1 or 2 (for a vehicle interface with 2 CAN controllers).

**id** - the CAN arbitration ID for the request.

**mode** - the OBD-II mode of the request - 1 through 15 (1 through 9 are the
    standardized modes).

**pid** - (optional) the PID for the request, if applicable.

**payload** - (optional) up to 7 bytes of data for the request's payload
    represented as a hexidecimal number in a string. Many JSON parser cannot
    handle 64-bit integers, which is why we are not using a numerical data type.
    Each byte in the string *must* be represented with 2 characters, e.g. `0x1`
    is `0x01` - the complete string must have an even number of characters.

**name** - (optional, defaults to nothing) A human readable, string name for
  this request. If provided, the response will have a `name` field (much like a
  normal translated message) with this value in place of `bus`, `id`, `mode` and
  `pid`.

**multiple_responses** - (optional, false by default) if true, request will stay
  active for a full 100ms, even after receiving a diagnostic response message.
  This is useful for requests to the functional broadcast arbitration ID
  (`0x7df`) when you need to get responses from multiple modules. It's possible
  to set this to `true` for non-broadcast requests, but in practice you won't
  see any additional responses after the first and it will just take up memory
  in the VI for longer.

**frequency** - (optional, defaults to 0) The frequency in Hz to send this
    request. To send a single non-recurring request, set this to 0 or leave it
    out.

**decoded_type** - (optional, defaults to "obd2" if the request is a recognized
OBD-II mode 1 request, otherwise "none") If specified, the valid values are
`"none"` and `"obd2"`. If `obd2`, the payload will be decoded according to the
OBD-II specification and returned in the `value` field. Set this to `none` to
manually override the OBD-II decoding feature for a known PID.

A diagnostic request's `bus`, `id`, `mode` and `pid` (or lack of a `pid`)
combine to create a unique key to identify a recurring request. This means that
you cannot simultaneosly have recurring requests at 2Hz and 5Hz for the same PID
from the same ID.

If you send a new `diagnostic_request` command with a `bus + id + mode + pid`
key matching an existing recurring request, it will update it with whatever
other parameters you've provided (e.g. it will change the frequency if you
specify one).

To cancel a recurring request, send a `diagnostic_request` command with the
matching request information (i.e. the `bus`, `id`, `mode` and `pid`) but a
frequency of 0.

Non-recurring requests may have the same `bus+id+mode(+pid)` key as a recurring
request, and they will co-exist without issue. As soon as a non-recurring
request is either completed or times out, it is removed from the active list.

If you're just requesting a PID, you can use this minimal field set for the
`request` object:

    {"bus": 1, "id": 1234, "mode": 1, "pid": 5}

### Responses

The response to a successful request:

    {"bus": 1,
      "id": 1234,
      "mode": 1,
      "pid": 5,
      "success": true,
      "payload": "0x1234",
      "value": 4660}

and to an unsuccessful request, with the `negative_response_code` and no `pid`
echo:

    {"bus": 1,
      "id": 1234,
      "mode": 1,
      "success": false,
      "negative_response_code": 17}

**bus** - the numerical identifier of the CAN bus where this response was
    received.

**id** - the CAN arbitration ID for this response.

**mode** - the OBD-II mode of the original diagnostic request.

**pid** - (optional) the PID for the request, if applicable.

**success** -  true if the response received was a positive response. If this
  field is false, the remote node returned an error and the
  `negative_response_code` field should be populated.

**negative_response_code** - (optional)  If requested node returned an error,
    `success` will be `false` and this field will contain the negative response
    code (NRC).

Finally, the `payload` and `value` fields are mutually exclusive:

**payload** - (optional) up to 7 bytes of data returned in the response,
    represented as a hexadecimal number in a string. Many JSON parser cannot
    handle 64-bit integers, which is why we are not using a numerical data type.

**value** - (optional) if the response had a payload, this may be the
    payload interpreted as an integer.

The response to a simple PID request would look like this:

    {"success": true, "bus": 1, "id": 1234, "mode": 1, "pid": 5, "payload": "0x2"}

## Commands

### Version Query

The `version` command triggers the VI to inject a firmware version identifier
response into the outgoing data stream.

**Request**

    { "command": "version"}

**Response**

    { "command_response": "version", "message": "v6.0-dev (default)"}

### Device ID Query

The `device_id` command triggers the VI to inject a unique device ID (e.g. the
MAC address of an included Bluetooth module) into into the outgoing data stream.

**Request**

    { "command": "device_id"}

**Response**

    { "command_response": "device_id", "message": "0012345678"}

## Trace File Format

An OpenXC vehicle trace file is a plaintext file that contains JSON objects,
separated by newlines (which may be either `\r\n` or `\n`, depending on the
platform the trace file was recorded).

The first line may be a metadata object, although this is optional:

```
{"metadata": {
    "version": "v3.0",
    "vehicle_interface_id": "7ABF",
    "vehicle": {
        "make": "Ford",
        "model": "Mustang",
        "trim": "V6 Premium",
        "year": 2013
    },
    "description": "highway drive to work",
    "driver_name": "TJ Giuli",
    "vehicle_id": "17N1039247929"
}
```

The following lines are OpenXC messages with a `timestamp` field added, e.g.:

    {"timestamp": 1385133351.285525, "name": "steering_wheel_angle", "value": 45}

The timestamp is in [UNIX time](http://en.wikipedia.org/wiki/Unix_time)
(i.e. seconds since the UNIX epoch, 00:00:00 UTC, 1/1/1970).

## Official Signals

These signal names are a part of the OpenXC specification, although some
manufacturers may support custom message names.

* steering_wheel_angle
    * numerical, -600 to +600 degrees
    * 10Hz
* torque_at_transmission
    * numerical, -500 to 1500 Nm
    * 10Hz
* engine_speed
    * numerical, 0 to 16382 RPM
    * 10Hz
* vehicle_speed
    * numerical, 0 to 655 km/h (this will be positive even if going in reverse
      as it's not a velocity, although you can use the gear status to figure out
      direction)
    * 10Hz
* accelerator_pedal_position
    * percentage
    * 10Hz
* parking_brake_status
    * boolean, (true == brake engaged)
    * 1Hz, but sent immediately on change
* brake_pedal_status
    * boolean (True == pedal pressed)
    * 1Hz, but sent immediately on change
* transmission_gear_position
    * states: first, second, third, fourth, fifth, sixth, seventh, eighth,
      ninth, tenth, reverse, neutral
    * 1Hz, but sent immediately on change
* gear_lever_position
    * states: neutral, park, reverse, drive, sport, low, first, second, third,
      fourth, fifth, sixth, seventh, eighth, ninth, tenth
    * 1Hz, but sent immediately on change
* odometer
    * Numerical, km
        0 to 16777214.000 km, with about .2m resolution
    * 10Hz
* ignition_status
    * states: off, accessory, run, start
    * 1Hz, but sent immediately on change
* fuel_level
    * percentage
    * 2Hz
* fuel_consumed_since_restart
    * numerical, 0 - 4294967295.0 L (this goes to 0 every time the vehicle
      restarts, like a trip meter)
    * 10Hz
* door_status
    * Value is State: driver, passenger, rear_left, rear_right.
    * Event is boolean: true == ajar
    * 1Hz, but sent immediately on change
* headlamp_status
    * boolean, true is on
    * 1Hz, but sent immediately on change
* high_beam_status
    * boolean, true is on
    * 1Hz, but sent immediately on change
* windshield_wiper_status
    * boolean, true is on
    * 1Hz, but sent immediately on change
* latitude
    * numerical, -89.0 to 89.0 degrees with standard GPS accuracy
    * 1Hz
* longitude
    * numerical, -179.0 to 179.0 degrees with standard GPS accuracy
    * 1Hz

### Signals from Diagnostics Messages

This set of signals is often retreived from OBD-II requests. The units can be
found in the [OBD-II standard](http://en.wikipedia.org/wiki/OBD-II_PIDs#Mode_01).

* engine_load
* engine_coolant_temperature
* barometric_pressure
* commanded_throttle_position
* throttle_position
* fuel_level
* intake_air_temperature
* intake_manifold_pressure
* running_time
* fuel_pressure
* mass_airflow
* accelerator_pedal_position
* ethanol_fuel_percentage
* engine_oil_temperature
* engine_torque

License
=======

Copyright (c) 2012-2014 Ford Motor Company

Licensed under the BSD license.

[OpenXC]: http://openxcplatform.com
