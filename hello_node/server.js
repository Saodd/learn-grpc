const messages = require('./hello_pb');
const services = require('./hello_grpc_pb');
const grpc = require('@grpc/grpc-js');


const echo = (call, callback) => {
    console.log(`收到: ${call.request.getSpeaker()} | ${call.request.getContent()}`)
    call.request.setSpeaker("Lewin-Server-Node")
    callback(null, call.request)
}

function main() {
    const server = new grpc.Server();
    server.addService(services.ChatService, {echo})
    server.bindAsync('0.0.0.0:5007', grpc.ServerCredentials.createInsecure(), () => {
        server.start();
    });
}

main()
