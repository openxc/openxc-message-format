# OpenXC Message Format Changelog

## v0.7.0

* Improvement: Increase diagnostic response payload size to accommodate
  multi-frame diagnostic responses.
* Feature: Added command to get device's platform

## v0.6.0

* Feature: Added MessagePack support for BTLE connections.
* Feature: Support for vehicle message timestamps (changed previous uptime).
* Feature: Support for C5 SD Card.
* Feature: Support for C5 RTC.
* Fix: Update submodule from code.google to github.

## v0.5.0

* Feature: Support for C5 Cellular device. New uptime message.

## v0.4

* BREAKING: Removed factor and offset from diagnostic requests to minimize the number of
  fields, and since this is such an uncommon use case and one that can be
  handled by the client receiving the data. We may add them back in the future.
* BREAKING: Require an 'action' to diagnostic request commands, e.g. cancel or add.
* BREAKING: Rename "raw" messages to the more precise "CAN messages".
* BREAKING: Rename "translated" messages to "simple messages".
* BREAKING: Remove redundant `type` field from simple messages (formerly
  translated messages). The type can be inferred implicitly through the types of
  the value and event fields.
* Feature: Add a command for controlling CAN message passthrough.
* Feature: Add a command for controlling CAN controller acceptance filter bypass.
* Feature: Add a command to change the payload format.
* Feature: Add a command to control whether pre-defined, recurring OBD-II
  requests are enabled.
* Improvement: Add `extras` field to JSON messages.
* Improvement: Add an optional 'status' field to all command responses.
* Improvement: Build protobuf generated files with nanopb v0.3.1.
* Improvement: Allow explicitly setting CAN message frame format (i.e. standard
  or extended frame).
* Fix: Expand range of mode field to a full byte (#10)

## v0.3

* Add diagnostic message request/response format.
* Officially add Protcol Buffer encoding.
* Change JSON delimiter to ```\0``` for both input and output.
* Officially document version and device ID commands.

## v0.2

* Add a RAW can message format.

## v0.1

* Initial release.
