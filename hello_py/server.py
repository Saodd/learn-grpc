import grpc
import hello_pb2_grpc
from concurrent import futures


class ChatServer(hello_pb2_grpc.ChatServicer):
    def Echo(self, sentence, context):
        print("收到: ", sentence)
        sentence.speaker = "Lewin-server-python"
        return sentence


if __name__ == '__main__':
    # 1. 服务器实例
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 2. 注册路由
    hello_pb2_grpc.add_ChatServicer_to_server(ChatServer(), server)
    # 3. 启动服务
    server.add_insecure_port('localhost:5006')
    server.start()
    server.wait_for_termination()