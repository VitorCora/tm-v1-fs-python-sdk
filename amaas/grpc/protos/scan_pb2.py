# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: amaas/grpc/protos/scan.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61maas/grpc/protos/scan.proto\x12\ramaas.scan.v1\"\xb3\x01\n\x03\x43\x32S\x12#\n\x05stage\x18\x01 \x01(\x0e\x32\x14.amaas.scan.v1.Stage\x12\x11\n\tfile_name\x18\x02 \x01(\t\x12\x0f\n\x07rs_size\x18\x03 \x01(\x05\x12\x0e\n\x06offset\x18\x04 \x01(\x05\x12\r\n\x05\x63hunk\x18\x05 \x01(\x0c\x12\x0e\n\x06trendx\x18\x06 \x01(\x08\x12\x11\n\tfile_sha1\x18\x07 \x01(\t\x12\x13\n\x0b\x66ile_sha256\x18\x08 \x01(\t\x12\x0c\n\x04tags\x18\t \x03(\t\"\x7f\n\x03S2C\x12#\n\x05stage\x18\x01 \x01(\x0e\x32\x14.amaas.scan.v1.Stage\x12#\n\x03\x63md\x18\x02 \x01(\x0e\x32\x16.amaas.scan.v1.Command\x12\x0e\n\x06offset\x18\x03 \x01(\x05\x12\x0e\n\x06length\x18\x04 \x01(\x05\x12\x0e\n\x06result\x18\x05 \x01(\t*6\n\x05Stage\x12\x0e\n\nSTAGE_INIT\x10\x00\x12\r\n\tSTAGE_RUN\x10\x01\x12\x0e\n\nSTAGE_FINI\x10\x02*%\n\x07\x43ommand\x12\x0c\n\x08\x43MD_RETR\x10\x00\x12\x0c\n\x08\x43MD_QUIT\x10\x01\x32;\n\x04Scan\x12\x33\n\x03Run\x12\x12.amaas.scan.v1.C2S\x1a\x12.amaas.scan.v1.S2C\"\x00(\x01\x30\x01\x42\x33\n\x1d\x63om.trend.cloudone.amaas.scanZ\x12\x61maas/scanner/baseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'amaas.grpc.protos.scan_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.trend.cloudone.amaas.scanZ\022amaas/scanner/base'
  _globals['_STAGE']._serialized_start=358
  _globals['_STAGE']._serialized_end=412
  _globals['_COMMAND']._serialized_start=414
  _globals['_COMMAND']._serialized_end=451
  _globals['_C2S']._serialized_start=48
  _globals['_C2S']._serialized_end=227
  _globals['_S2C']._serialized_start=229
  _globals['_S2C']._serialized_end=356
  _globals['_SCAN']._serialized_start=453
  _globals['_SCAN']._serialized_end=512
# @@protoc_insertion_point(module_scope)
