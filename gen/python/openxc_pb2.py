# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openxc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='openxc.proto',
  package='openxc',
  serialized_pb='\n\x0copenxc.proto\x12\x06openxc\"\xbc\x01\n\x0eVehicleMessage\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.openxc.VehicleMessage.Type\x12\'\n\x0braw_message\x18\x02 \x01(\x0b\x32\x12.openxc.RawMessage\x12\x35\n\x12translated_message\x18\x03 \x01(\x0b\x32\x19.openxc.TranslatedMessage\"\x1f\n\x04Type\x12\x07\n\x03RAW\x10\x01\x12\x0e\n\nTRANSLATED\x10\x02\";\n\nRawMessage\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x12\n\nmessage_id\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x04\"\x91\x01\n\x11\x44iagnosticMessage\x12\x0b\n\x03\x62us\x18\x01 \x01(\x05\x12\x12\n\nmessage_id\x18\x02 \x01(\r\x12\x0c\n\x04mode\x18\x03 \x01(\r\x12\x0b\n\x03pid\x18\x04 \x01(\r\x12\x0f\n\x07success\x18\x05 \x01(\x08\x12\x1e\n\x16negative_response_code\x18\x06 \x01(\r\x12\x0f\n\x07payload\x18\x07 \x01(\x04\"\xb5\x02\n\x11TranslatedMessage\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.openxc.TranslatedMessage.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cstring_value\x18\x03 \x01(\t\x12\x15\n\rnumeric_value\x18\x04 \x01(\x01\x12\x15\n\rboolean_value\x18\x05 \x01(\x08\x12\x14\n\x0cstring_event\x18\x06 \x01(\t\x12\x15\n\rnumeric_event\x18\x07 \x01(\x01\x12\x15\n\rboolean_event\x18\x08 \x01(\x08\"\\\n\x04Type\x12\n\n\x06STRING\x10\x01\x12\x07\n\x03NUM\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x12\x12\n\x0e\x45VENTED_STRING\x10\x04\x12\x0f\n\x0b\x45VENTED_NUM\x10\x05\x12\x10\n\x0c\x45VENTED_BOOL\x10\x06\x42\x1c\n\ncom.openxcB\x0e\x42inaryMessages')



_VEHICLEMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='openxc.VehicleMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAW', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSLATED', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=182,
  serialized_end=213,
)

_TRANSLATEDMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='openxc.TranslatedMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUM', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENTED_STRING', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENTED_NUM', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EVENTED_BOOL', index=5, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=642,
  serialized_end=734,
)


_VEHICLEMESSAGE = _descriptor.Descriptor(
  name='VehicleMessage',
  full_name='openxc.VehicleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.VehicleMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_message', full_name='openxc.VehicleMessage.raw_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='translated_message', full_name='openxc.VehicleMessage.translated_message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VEHICLEMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=25,
  serialized_end=213,
)


_RAWMESSAGE = _descriptor.Descriptor(
  name='RawMessage',
  full_name='openxc.RawMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.RawMessage.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='openxc.RawMessage.message_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='openxc.RawMessage.data', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=215,
  serialized_end=274,
)


_DIAGNOSTICMESSAGE = _descriptor.Descriptor(
  name='DiagnosticMessage',
  full_name='openxc.DiagnosticMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bus', full_name='openxc.DiagnosticMessage.bus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='openxc.DiagnosticMessage.message_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='openxc.DiagnosticMessage.mode', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pid', full_name='openxc.DiagnosticMessage.pid', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='success', full_name='openxc.DiagnosticMessage.success', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negative_response_code', full_name='openxc.DiagnosticMessage.negative_response_code', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='openxc.DiagnosticMessage.payload', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=277,
  serialized_end=422,
)


_TRANSLATEDMESSAGE = _descriptor.Descriptor(
  name='TranslatedMessage',
  full_name='openxc.TranslatedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='openxc.TranslatedMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='openxc.TranslatedMessage.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='openxc.TranslatedMessage.string_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numeric_value', full_name='openxc.TranslatedMessage.numeric_value', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boolean_value', full_name='openxc.TranslatedMessage.boolean_value', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_event', full_name='openxc.TranslatedMessage.string_event', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numeric_event', full_name='openxc.TranslatedMessage.numeric_event', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boolean_event', full_name='openxc.TranslatedMessage.boolean_event', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSLATEDMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=425,
  serialized_end=734,
)

_VEHICLEMESSAGE.fields_by_name['type'].enum_type = _VEHICLEMESSAGE_TYPE
_VEHICLEMESSAGE.fields_by_name['raw_message'].message_type = _RAWMESSAGE
_VEHICLEMESSAGE.fields_by_name['translated_message'].message_type = _TRANSLATEDMESSAGE
_VEHICLEMESSAGE_TYPE.containing_type = _VEHICLEMESSAGE;
_TRANSLATEDMESSAGE.fields_by_name['type'].enum_type = _TRANSLATEDMESSAGE_TYPE
_TRANSLATEDMESSAGE_TYPE.containing_type = _TRANSLATEDMESSAGE;
DESCRIPTOR.message_types_by_name['VehicleMessage'] = _VEHICLEMESSAGE
DESCRIPTOR.message_types_by_name['RawMessage'] = _RAWMESSAGE
DESCRIPTOR.message_types_by_name['DiagnosticMessage'] = _DIAGNOSTICMESSAGE
DESCRIPTOR.message_types_by_name['TranslatedMessage'] = _TRANSLATEDMESSAGE

class VehicleMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VEHICLEMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.VehicleMessage)

class RawMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RAWMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.RawMessage)

class DiagnosticMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIAGNOSTICMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.DiagnosticMessage)

class TranslatedMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSLATEDMESSAGE

  # @@protoc_insertion_point(class_scope:openxc.TranslatedMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\ncom.openxcB\016BinaryMessages')
# @@protoc_insertion_point(module_scope)
