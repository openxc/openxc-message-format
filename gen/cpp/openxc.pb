
Ã
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
data ("¦
ControlCommand)
type (2.openxc.ControlCommand.Type5
diagnostic_request (2.openxc.DiagnosticRequest"2
Type
VERSION
	DEVICE_ID

DIAGNOSTIC"M
CommandResponse)
type (2.openxc.ControlCommand.Type
message (	"ý
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