
«	
openxc.protoopenxc"…
VehicleMessage)
type (2.openxc.VehicleMessage.Type'
raw_message (2.openxc.RawMessage5
translated_message (2.openxc.TranslatedMessage7
diagnostic_response (2.openxc.DiagnosticResponse"/
Type
RAW

TRANSLATED

DIAGNOSTIC";

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

DIAGNOSTIC"ª
DiagnosticRequest
bus (

message_id (
mode (
pid (
payload (
parse_payload (
factor (
offset (
	frequency	 ("¡
DiagnosticResponse
bus (

message_id (
mode (
pid (
success (
negative_response_code (
payload (
value ("µ
TranslatedMessage,
type (2.openxc.TranslatedMessage.Type
name (	
string_value (	
numeric_value (
boolean_value (
string_event (	
numeric_event (
boolean_event ("\
Type

STRING
NUM
BOOL
EVENTED_STRING
EVENTED_NUM
EVENTED_BOOLB

com.openxcBBinaryMessages