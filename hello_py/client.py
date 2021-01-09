import grpc
import hello_pb2_grpc
import hello_pb2

if __name__ == '__main__':
    # 1. 建立连接，准备客户端
    channel = grpc.insecure_channel("localhost:5006")
    stub = hello_pb2_grpc.ChatStub(channel)

    # 2. 调用
    req = hello_pb2.Sentence(speaker="Lewin-Client-Python", content="Hello, world!! from python.")
    resp = stub.Echo(req)
    print(resp)
