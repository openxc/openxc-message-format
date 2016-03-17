# OpenXC Message Format Specification

Version: v0.6.0

This specification is a part of the [OpenXC platform][OpenXC].

An OpenXC vehicle interface sends generic vehicle data over one or more output
interfaces (e.g. USB or Bluetooth) as JSON or Protocol Buffers (protobuf).

## JSON

The JSON format is the most flexible and easiest to use. The format is fully
specified in the [JSON.mkd](JSON.mkd) file in this repository.
a more flexible option than binary, but is less compact and
therefore takes more bandwidth and processing power.

The JSON format is best for most developers, as it is fairly efficient and very
flexible.

## Binary (Protocol Buffers)

The binary format is encoded using [Google Protocol
Buffers](https://code.google.com/p/protobuf/). The format is specified in the
file [openxc.proto](openxc.proto). The descriptions of the messages can be foud
in the JSON specs - the binary format mirrors this.

The binary messages are published by the VI using the standard length-delimited
method (any protobuf library should support this).

The binary format is best if you need to maximize the amount of data that can be
sent from the VI, trading off flexibility for efficiency.

## Message Pack
MessagePack is an efficient binary serialization format. It lets you exchange data
among multiple languages like JSON, but it's faster and smaller. Small integers are 
encoded into a single byte, and typical short strings require only one extra byte
in addition to the strings themselves

For protocol specification visit:
https://github.com/msgpack/msgpack/blob/master/spec.md

We are using the following lib:
https://github.com/camgunz/cmp

MessagePack provides a binary alternative to ProtoBuf. There are pros & cons to each 
so you can decide what works best for your project.

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

## Signals from Diagnostic Messages

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
