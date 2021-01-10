const messages = require('./hello_pb');
const services = require('./hello_grpc_pb');
const grpc = require('@grpc/grpc-js');

function main() {
    // 1. 建立连接
    const client = new services.ChatClient("localhost:5007", grpc.credentials.createInsecure())

    // 2. 准备请求数据。
    // 这里很恐怖的是，初始化数据居然是通过Array传入的……所以强烈建议使用setXXX方法来准备参数……
    const req = new messages.Sentence(["Lewin-Client-Node", "Hello, world!"])
    req.setContent("Hello, 世界!")
    console.log(`发送: ${req.getSpeaker()} | ${req.getContent()}`)

    // 3. 执行调用。
    client.echo(req, function (err, resp) {
        console.log(`结果: ${err} | ${resp.getSpeaker()} | ${resp.getContent()}`)
    })
}

main()
