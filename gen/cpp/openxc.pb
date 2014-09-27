
Á
openxc.protoopenxc"”
VehicleMessage)
type (2.openxc.VehicleMessage.Type'
raw_message (2.openxc.RawMessage5
translated_message (2.openxc.TranslatedMessage7
diagnostic_response (2.openxc.DiagnosticResponse/
control_command (2.openxc.ControlCommand1
command_response (2.openxc.CommandResponse"Z
Type
RAW

TRANSLATED

DIAGNOSTIC
CONTROL_COMMAND
COMMAND_RESPONSE";

RawMessage
bus (

message_id (
data ("ö
ControlCommand)
type (2.openxc.ControlCommand.Type<
diagnostic_request (2 .openxc.DiagnosticControlCommandG
passthrough_mode_request (2%.openxc.PassthroughModeControlCommandO
 acceptance_filter_bypass_command (2%.openxc.AcceptanceFilterBypassCommand"a
Type
VERSION
	DEVICE_ID

DIAGNOSTIC
PASSTHROUGH
ACCEPTANCE_FILTER_BYPASS"ž
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
bypass ("]
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
BOOL"÷
TranslatedMessage,
type (2.openxc.TranslatedMessage.Type
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