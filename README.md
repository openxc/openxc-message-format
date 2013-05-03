# OpenXC Message Format Specification

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
