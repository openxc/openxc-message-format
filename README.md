# OpenXC Message Format Specification

This specification is a part of the [OpenXC platform][OpenXC].

An OpenXC vehicle interface sends generic vehicle data over one or more output
interfaces (e.g. USB or Bluetooth) as JSON objects, separated by newlines.

There are two valid message types - single valued and evented.

There may not be a 1:1 relationship between input and output signals - i.e. raw
engine timing CAN signals may be summarized in an "engine performance" metric on
the abstract side of the interface.

## Single Valued

The expected format of a single valued message is:

    {"name": "steering_wheel_angle", "value": 45}

## Evented

The expected format of an event message is:

    {"name": "button_event", "value": "up", "event": "pressed"}

This format is good for something like a button event, where there are two
discrete pieces of information in the measurement.

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
      reverse, neutral
    * 1Hz, but sent immediately on change
* gear_lever_position
    * states: neutral, park, reverse, drive, sport, low, first, second, third,
      fourth, fifth, sixth
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

## Raw CAN Message format

An OpenXC vehicle interface may also output raw CAN messages. Each CAN message
is sent as a JSON object, separated by newlines. The format of each object is:

    {"bus": 1, "id": 1234, "value": "0x12345678"}

**bus** - the numerical identifier of the CAN bus where this message originated,
  most likely 1 or 2 (for a vehicle interface with 2 CAN controllers).

**id** - the CAN message ID

**data** - up to 8 bytes of data from the CAN message's payload, represented as
  a hexidecimal number in a string. Many JSON parser cannot handle 64-bit
  integers, which is why we are not using a numerical data type.

License
=======

Copyright (c) 2012-2013 Ford Motor Company

Licensed under the BSD license.

[OpenXC]: http://openxcplatform.com
