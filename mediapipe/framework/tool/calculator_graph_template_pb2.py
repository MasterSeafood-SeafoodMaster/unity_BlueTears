# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/tool/calculator_graph_template.proto

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
from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.framework.deps import proto_descriptor_pb2 as mediapipe_dot_framework_dot_deps_dot_proto__descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/tool/calculator_graph_template.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n8mediapipe/framework/tool/calculator_graph_template.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a/mediapipe/framework/deps/proto_descriptor.proto\"\xf0\x01\n\x12TemplateExpression\x12\r\n\x05param\x18\x01 \x01(\t\x12\n\n\x02op\x18\x02 \x01(\t\x12*\n\x03\x61rg\x18\x03 \x03(\x0b\x32\x1d.mediapipe.TemplateExpression\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x38\n\nfield_type\x18\x05 \x01(\x0e\x32$.mediapipe.FieldDescriptorProto.Type\x12\x36\n\x08key_type\x18\x06 \x03(\x0e\x32$.mediapipe.FieldDescriptorProto.Type\x12\x13\n\x0b\x66ield_value\x18\x07 \x01(\t\"x\n\x17\x43\x61lculatorGraphTemplate\x12\x30\n\x06\x63onfig\x18\x01 \x01(\x0b\x32 .mediapipe.CalculatorGraphConfig\x12+\n\x04rule\x18\x02 \x03(\x0b\x32\x1d.mediapipe.TemplateExpression\"\x96\x01\n\x10TemplateArgument\x12\r\n\x03str\x18\x01 \x01(\tH\x00\x12\r\n\x03num\x18\x02 \x01(\x01H\x00\x12\'\n\x04\x64ict\x18\x03 \x01(\x0b\x32\x17.mediapipe.TemplateDictH\x00\x12,\n\x07\x65lement\x18\x04 \x03(\x0b\x32\x1b.mediapipe.TemplateArgumentB\r\n\x0bparam_value\"\x84\x01\n\x0cTemplateDict\x12.\n\x03\x61rg\x18\x01 \x03(\x0b\x32!.mediapipe.TemplateDict.Parameter\x1a\x44\n\tParameter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.mediapipe.TemplateArgument\"\x92\x01\n\x17TemplateSubgraphOptions\x12%\n\x04\x64ict\x18\x01 \x01(\x0b\x32\x17.mediapipe.TemplateDict2P\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf5\xfc\xbeR \x01(\x0b\x32\".mediapipe.TemplateSubgraphOptionsB0\n\x1a\x63om.google.mediapipe.protoB\x12GraphTemplateProto')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_calculator__options__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_deps_dot_proto__descriptor__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TEMPLATEEXPRESSION = _descriptor.Descriptor(
  name='TemplateExpression',
  full_name='mediapipe.TemplateExpression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param', full_name='mediapipe.TemplateExpression.param', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op', full_name='mediapipe.TemplateExpression.op', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arg', full_name='mediapipe.TemplateExpression.arg', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='mediapipe.TemplateExpression.path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_type', full_name='mediapipe.TemplateExpression.field_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key_type', full_name='mediapipe.TemplateExpression.key_type', index=5,
      number=6, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_value', full_name='mediapipe.TemplateExpression.field_value', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=445,
)


_CALCULATORGRAPHTEMPLATE = _descriptor.Descriptor(
  name='CalculatorGraphTemplate',
  full_name='mediapipe.CalculatorGraphTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='mediapipe.CalculatorGraphTemplate.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rule', full_name='mediapipe.CalculatorGraphTemplate.rule', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=567,
)


_TEMPLATEARGUMENT = _descriptor.Descriptor(
  name='TemplateArgument',
  full_name='mediapipe.TemplateArgument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='str', full_name='mediapipe.TemplateArgument.str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='mediapipe.TemplateArgument.num', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dict', full_name='mediapipe.TemplateArgument.dict', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='element', full_name='mediapipe.TemplateArgument.element', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='param_value', full_name='mediapipe.TemplateArgument.param_value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=570,
  serialized_end=720,
)


_TEMPLATEDICT_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='mediapipe.TemplateDict.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mediapipe.TemplateDict.Parameter.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='mediapipe.TemplateDict.Parameter.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=787,
  serialized_end=855,
)

_TEMPLATEDICT = _descriptor.Descriptor(
  name='TemplateDict',
  full_name='mediapipe.TemplateDict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arg', full_name='mediapipe.TemplateDict.arg', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TEMPLATEDICT_PARAMETER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=723,
  serialized_end=855,
)


_TEMPLATESUBGRAPHOPTIONS = _descriptor.Descriptor(
  name='TemplateSubgraphOptions',
  full_name='mediapipe.TemplateSubgraphOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dict', full_name='mediapipe.TemplateSubgraphOptions.dict', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TemplateSubgraphOptions.ext', index=0,
      number=172998261, type=11, cpp_type=10, label=1,
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
  serialized_start=858,
  serialized_end=1004,
)

_TEMPLATEEXPRESSION.fields_by_name['arg'].message_type = _TEMPLATEEXPRESSION
_TEMPLATEEXPRESSION.fields_by_name['field_type'].enum_type = mediapipe_dot_framework_dot_deps_dot_proto__descriptor__pb2._FIELDDESCRIPTORPROTO_TYPE
_TEMPLATEEXPRESSION.fields_by_name['key_type'].enum_type = mediapipe_dot_framework_dot_deps_dot_proto__descriptor__pb2._FIELDDESCRIPTORPROTO_TYPE
_CALCULATORGRAPHTEMPLATE.fields_by_name['config'].message_type = mediapipe_dot_framework_dot_calculator__pb2._CALCULATORGRAPHCONFIG
_CALCULATORGRAPHTEMPLATE.fields_by_name['rule'].message_type = _TEMPLATEEXPRESSION
_TEMPLATEARGUMENT.fields_by_name['dict'].message_type = _TEMPLATEDICT
_TEMPLATEARGUMENT.fields_by_name['element'].message_type = _TEMPLATEARGUMENT
_TEMPLATEARGUMENT.oneofs_by_name['param_value'].fields.append(
  _TEMPLATEARGUMENT.fields_by_name['str'])
_TEMPLATEARGUMENT.fields_by_name['str'].containing_oneof = _TEMPLATEARGUMENT.oneofs_by_name['param_value']
_TEMPLATEARGUMENT.oneofs_by_name['param_value'].fields.append(
  _TEMPLATEARGUMENT.fields_by_name['num'])
_TEMPLATEARGUMENT.fields_by_name['num'].containing_oneof = _TEMPLATEARGUMENT.oneofs_by_name['param_value']
_TEMPLATEARGUMENT.oneofs_by_name['param_value'].fields.append(
  _TEMPLATEARGUMENT.fields_by_name['dict'])
_TEMPLATEARGUMENT.fields_by_name['dict'].containing_oneof = _TEMPLATEARGUMENT.oneofs_by_name['param_value']
_TEMPLATEDICT_PARAMETER.fields_by_name['value'].message_type = _TEMPLATEARGUMENT
_TEMPLATEDICT_PARAMETER.containing_type = _TEMPLATEDICT
_TEMPLATEDICT.fields_by_name['arg'].message_type = _TEMPLATEDICT_PARAMETER
_TEMPLATESUBGRAPHOPTIONS.fields_by_name['dict'].message_type = _TEMPLATEDICT
DESCRIPTOR.message_types_by_name['TemplateExpression'] = _TEMPLATEEXPRESSION
DESCRIPTOR.message_types_by_name['CalculatorGraphTemplate'] = _CALCULATORGRAPHTEMPLATE
DESCRIPTOR.message_types_by_name['TemplateArgument'] = _TEMPLATEARGUMENT
DESCRIPTOR.message_types_by_name['TemplateDict'] = _TEMPLATEDICT
DESCRIPTOR.message_types_by_name['TemplateSubgraphOptions'] = _TEMPLATESUBGRAPHOPTIONS

TemplateExpression = _reflection.GeneratedProtocolMessageType('TemplateExpression', (_message.Message,), dict(
  DESCRIPTOR = _TEMPLATEEXPRESSION,
  __module__ = 'mediapipe.framework.tool.calculator_graph_template_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TemplateExpression)
  ))
_sym_db.RegisterMessage(TemplateExpression)

CalculatorGraphTemplate = _reflection.GeneratedProtocolMessageType('CalculatorGraphTemplate', (_message.Message,), dict(
  DESCRIPTOR = _CALCULATORGRAPHTEMPLATE,
  __module__ = 'mediapipe.framework.tool.calculator_graph_template_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.CalculatorGraphTemplate)
  ))
_sym_db.RegisterMessage(CalculatorGraphTemplate)

TemplateArgument = _reflection.GeneratedProtocolMessageType('TemplateArgument', (_message.Message,), dict(
  DESCRIPTOR = _TEMPLATEARGUMENT,
  __module__ = 'mediapipe.framework.tool.calculator_graph_template_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TemplateArgument)
  ))
_sym_db.RegisterMessage(TemplateArgument)

TemplateDict = _reflection.GeneratedProtocolMessageType('TemplateDict', (_message.Message,), dict(

  Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
    DESCRIPTOR = _TEMPLATEDICT_PARAMETER,
    __module__ = 'mediapipe.framework.tool.calculator_graph_template_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.TemplateDict.Parameter)
    ))
  ,
  DESCRIPTOR = _TEMPLATEDICT,
  __module__ = 'mediapipe.framework.tool.calculator_graph_template_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TemplateDict)
  ))
_sym_db.RegisterMessage(TemplateDict)
_sym_db.RegisterMessage(TemplateDict.Parameter)

TemplateSubgraphOptions = _reflection.GeneratedProtocolMessageType('TemplateSubgraphOptions', (_message.Message,), dict(
  DESCRIPTOR = _TEMPLATESUBGRAPHOPTIONS,
  __module__ = 'mediapipe.framework.tool.calculator_graph_template_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TemplateSubgraphOptions)
  ))
_sym_db.RegisterMessage(TemplateSubgraphOptions)

_TEMPLATESUBGRAPHOPTIONS.extensions_by_name['ext'].message_type = _TEMPLATESUBGRAPHOPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TEMPLATESUBGRAPHOPTIONS.extensions_by_name['ext'])

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.google.mediapipe.protoB\022GraphTemplateProto'))
# @@protoc_insertion_point(module_scope)
