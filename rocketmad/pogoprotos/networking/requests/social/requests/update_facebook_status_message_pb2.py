# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/social/requests/update_facebook_status_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/social/requests/update_facebook_status_message.proto',
  package='pogoprotos.networking.requests.social.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nSpogoprotos/networking/requests/social/requests/update_facebook_status_message.proto\x12.pogoprotos.networking.requests.social.requests\"L\n\x1bUpdateFacebookStatusMessage\x12\x17\n\x0f\x66\x62_access_token\x18\x01 \x01(\t\x12\x14\n\x0c\x66orce_update\x18\x02 \x01(\x08\x62\x06proto3')
)




_UPDATEFACEBOOKSTATUSMESSAGE = _descriptor.Descriptor(
  name='UpdateFacebookStatusMessage',
  full_name='pogoprotos.networking.requests.social.requests.UpdateFacebookStatusMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fb_access_token', full_name='pogoprotos.networking.requests.social.requests.UpdateFacebookStatusMessage.fb_access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='force_update', full_name='pogoprotos.networking.requests.social.requests.UpdateFacebookStatusMessage.force_update', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=135,
  serialized_end=211,
)

DESCRIPTOR.message_types_by_name['UpdateFacebookStatusMessage'] = _UPDATEFACEBOOKSTATUSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateFacebookStatusMessage = _reflection.GeneratedProtocolMessageType('UpdateFacebookStatusMessage', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEFACEBOOKSTATUSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.social.requests.update_facebook_status_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.social.requests.UpdateFacebookStatusMessage)
  ))
_sym_db.RegisterMessage(UpdateFacebookStatusMessage)


# @@protoc_insertion_point(module_scope)
