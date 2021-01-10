// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var hello_pb = require('./hello_pb.js');

function serialize_Sentence(arg) {
  if (!(arg instanceof hello_pb.Sentence)) {
    throw new Error('Expected argument of type Sentence');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_Sentence(buffer_arg) {
  return hello_pb.Sentence.deserializeBinary(new Uint8Array(buffer_arg));
}


var ChatService = exports.ChatService = {
  echo: {
    path: '/Chat/Echo',
    requestStream: false,
    responseStream: false,
    requestType: hello_pb.Sentence,
    responseType: hello_pb.Sentence,
    requestSerialize: serialize_Sentence,
    requestDeserialize: deserialize_Sentence,
    responseSerialize: serialize_Sentence,
    responseDeserialize: deserialize_Sentence,
  },
};

exports.ChatClient = grpc.makeGenericClientConstructor(ChatService);
