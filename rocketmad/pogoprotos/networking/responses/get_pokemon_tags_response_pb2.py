# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_pokemon_tags_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.requests.messages import edit_pokemon_tag_message_pb2 as pogoprotos_dot_networking_dot_requests_dot_messages_dot_edit__pokemon__tag__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_pokemon_tags_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?pogoprotos/networking/responses/get_pokemon_tags_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x46pogoprotos/networking/requests/messages/edit_pokemon_tag_message.proto\"\x82\x02\n\x16GetPokemonTagsResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.pogoprotos.networking.responses.GetPokemonTagsResponse.Result\x12V\n\x03tag\x18\x02 \x03(\x0b\x32I.pogoprotos.networking.requests.messages.EditPokemonTagMessage.PokemonTag\"@\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1e\n\x1a\x45RROR_PLAYER_LEVEL_TOO_LOW\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_networking_dot_requests_dot_messages_dot_edit__pokemon__tag__message__pb2.DESCRIPTOR,])



_GETPOKEMONTAGSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetPokemonTagsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_LEVEL_TOO_LOW', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=367,
  serialized_end=431,
)
_sym_db.RegisterEnumDescriptor(_GETPOKEMONTAGSRESPONSE_RESULT)


_GETPOKEMONTAGSRESPONSE = _descriptor.Descriptor(
  name='GetPokemonTagsResponse',
  full_name='pogoprotos.networking.responses.GetPokemonTagsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetPokemonTagsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='pogoprotos.networking.responses.GetPokemonTagsResponse.tag', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETPOKEMONTAGSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=431,
)

_GETPOKEMONTAGSRESPONSE.fields_by_name['result'].enum_type = _GETPOKEMONTAGSRESPONSE_RESULT
_GETPOKEMONTAGSRESPONSE.fields_by_name['tag'].message_type = pogoprotos_dot_networking_dot_requests_dot_messages_dot_edit__pokemon__tag__message__pb2._EDITPOKEMONTAGMESSAGE_POKEMONTAG
_GETPOKEMONTAGSRESPONSE_RESULT.containing_type = _GETPOKEMONTAGSRESPONSE
DESCRIPTOR.message_types_by_name['GetPokemonTagsResponse'] = _GETPOKEMONTAGSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPokemonTagsResponse = _reflection.GeneratedProtocolMessageType('GetPokemonTagsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPOKEMONTAGSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_pokemon_tags_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetPokemonTagsResponse)
  ))
_sym_db.RegisterMessage(GetPokemonTagsResponse)


# @@protoc_insertion_point(module_scope)