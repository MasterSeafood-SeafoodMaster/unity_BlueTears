# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/packet_cloner_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/core/packet_cloner_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n9mediapipe/calculators/core/packet_cloner_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xe9\x01\n\x1dPacketClonerCalculatorOptions\x12\x33\n$output_only_when_all_inputs_received\x18\x01 \x01(\x08:\x05\x66\x61lse\x12;\n,output_packets_only_when_all_inputs_received\x18\x02 \x01(\x08:\x05\x66\x61lse2V\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x95\xa6\xb8{ \x01(\x0b\x32(.mediapipe.PacketClonerCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PACKETCLONERCALCULATOROPTIONS = _descriptor.Descriptor(
  name='PacketClonerCalculatorOptions',
  full_name='mediapipe.PacketClonerCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_only_when_all_inputs_received', full_name='mediapipe.PacketClonerCalculatorOptions.output_only_when_all_inputs_received', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_packets_only_when_all_inputs_received', full_name='mediapipe.PacketClonerCalculatorOptions.output_packets_only_when_all_inputs_received', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.PacketClonerCalculatorOptions.ext', index=0,
      number=258872085, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=344,
)

DESCRIPTOR.message_types_by_name['PacketClonerCalculatorOptions'] = _PACKETCLONERCALCULATOROPTIONS

PacketClonerCalculatorOptions = _reflection.GeneratedProtocolMessageType('PacketClonerCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _PACKETCLONERCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.core.packet_cloner_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.PacketClonerCalculatorOptions)
  ))
_sym_db.RegisterMessage(PacketClonerCalculatorOptions)

_PACKETCLONERCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _PACKETCLONERCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_PACKETCLONERCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
