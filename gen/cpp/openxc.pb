
€
openxc.protoopenxc"ˆ
VehicleMessage)
type (2.openxc.VehicleMessage.Type'
can_message (2.openxc.CanMessage-
simple_message (2.openxc.SimpleMessage7
diagnostic_response (2.openxc.DiagnosticResponse/
control_command (2.openxc.ControlCommand1
command_response (2.openxc.CommandResponse"V
Type
CAN

SIMPLE

DIAGNOSTIC
CONTROL_COMMAND
COMMAND_RESPONSE"œ

CanMessage
bus (

message_id (
data (4
frame_format (2.openxc.CanMessage.FrameFormat")
FrameFormat
STANDARD
EXTENDED"¸
ControlCommand)
type (2.openxc.ControlCommand.Type<
diagnostic_request (2 .openxc.DiagnosticControlCommandG
passthrough_mode_request (2%.openxc.PassthroughModeControlCommandO
 acceptance_filter_bypass_command (2%.openxc.AcceptanceFilterBypassCommand<
payload_format_command (2.openxc.PayloadFormatCommandO
 predefined_obd2_requests_command (2%.openxc.PredefinedObd2RequestsCommand"“
Type
VERSION
	DEVICE_ID

DIAGNOSTIC
PASSTHROUGH
ACCEPTANCE_FILTER_BYPASS
PAYLOAD_FORMAT
PREDEFINED_OBD2_REQUESTS"ž
DiagnosticControlCommand*
request (2.openxc.DiagnosticRequest7
action (2'.openxc.DiagnosticControlCommand.Action"
Action
ADD

CANCEL"=
PassthroughModeControlCommand
bus (
enabled ("<
AcceptanceFilterBypassCommand
bus (
bypass ("{
PayloadFormatCommand:
format (2*.openxc.PayloadFormatCommand.PayloadFormat"'
PayloadFormat
JSON
PROTOBUF"0
PredefinedObd2RequestsCommand
enabled ("]
CommandResponse)
type (2.openxc.ControlCommand.Type
message (	
status ("ý
DiagnosticRequest
bus (

message_id (
mode (
pid (
payload (
multiple_responses (
	frequency (
name (	;
decoded_type	 (2%.openxc.DiagnosticRequest.DecodedType"!
DecodedType
NONE
OBD2"¡
DiagnosticResponse
bus (

message_id (
mode (
pid (
success (
negative_response_code (
payload (
value ("¢
DynamicField'
type (2.openxc.DynamicField.Type
string_value (	
numeric_value (
boolean_value ("%
Type

STRING
NUM
BOOL"ï
SimpleMessage(
type (2.openxc.SimpleMessage.Type
name (	#
value (2.openxc.DynamicField#
event (2.openxc.DynamicField"\
Type

STRING
NUM
BOOL
EVENTED_STRING
EVENTED_NUM
EVENTED_BOOLB

com.openxcBBinaryMessages