# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z\n.;hello_go',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bhello.proto\",\n\x08Sentence\x12\x0f\n\x07speaker\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t2$\n\x04\x43hat\x12\x1c\n\x04\x45\x63ho\x12\t.Sentence\x1a\t.SentenceB\x0cZ\n.;hello_gob\x06proto3'
)




_SENTENCE = _descriptor.Descriptor(
  name='Sentence',
  full_name='Sentence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='speaker', full_name='Sentence.speaker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='Sentence.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=59,
)

DESCRIPTOR.message_types_by_name['Sentence'] = _SENTENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sentence = _reflection.GeneratedProtocolMessageType('Sentence', (_message.Message,), {
  'DESCRIPTOR' : _SENTENCE,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:Sentence)
  })
_sym_db.RegisterMessage(Sentence)


DESCRIPTOR._options = None

_CHAT = _descriptor.ServiceDescriptor(
  name='Chat',
  full_name='Chat',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=61,
  serialized_end=97,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='Chat.Echo',
    index=0,
    containing_service=None,
    input_type=_SENTENCE,
    output_type=_SENTENCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHAT)

DESCRIPTOR.services_by_name['Chat'] = _CHAT

# @@protoc_insertion_point(module_scope)