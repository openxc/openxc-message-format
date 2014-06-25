# OpenXC Message Format Changelog

## v0.4-dev

* Removed factor and offset from diagnostic requests to minimize the number of
  fields, and since this is such an uncommon use case and one that can be
  handled by the client receiving the data. We may add them back in the future.
* Add `extras` field to JSON messages.

## v0.3

* Add diagnostic message request/response format.
* Officially add Protcol Buffer encoding.
* Change JSON delimiter to ```\0``` for both input and output.
* Officially document version and device ID commands.

## v0.2

* Add a RAW can message format.

## v0.1

* Initial release.
