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
    * numerical, degrees
* torque_at_transmission
    * numerical, Nm
* engine_speed
    * numerical, RPM
* vehicle_speed, numerical, Kph
* accelerator_pedal_position
    * percentage
* parking_brake_status
    * boolean, (true == brake engaged)
* brake_pedal_status
    * boolean (True == pedal pressed)
* transmission_gear_position
    * states: first, second, third, fourth, fifth, sixth, seventh, eighth,
      reverse, neutral
* odometer
    * Numerical, km
* ignition_status
    * states: off, accessory, run, start
* fuel_level
    * percentage
* fuel_consumed_since_restart
    * numerical, liters (goes to 0 every time the
  vehicle interfaces power cycles)
* door_status
    * Value is State: driver, passenger, rear_left, rear_right.
    * Event is boolean: true == ajar
* headlamp_status
    * boolean, true is on
* high_beam_status
    * boolean, true is on
* windshield_wiper_status
    * boolean, true is on
* latitude
    * numerical
* longitude
    * numerical

License
=======

Copyright (c) 2012-2013 Ford Motor Company

Licensed under the BSD license.

[OpenXC]: http://openxcplatform.com
