package main

import (
	"context"
	"fmt"
	"github.com/Saodd/learn-grpc/hello_go"
	"google.golang.org/grpc"
	"log"
	"net"
)

type ChatServer struct {
	hello_go.ChatServer
}

func (s *ChatServer) Echo(ctx context.Context, sentence *hello_go.Sentence) (*hello_go.Sentence, error) {
	fmt.Println("收到: ", sentence)
	sentence.Speaker = "Lewin-Server"
	return sentence, nil
}

func main() {
	lis, err := net.Listen("tcp", "localhost:5005")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	grpcServer := grpc.NewServer()
	hello_go.RegisterChatServer(grpcServer, &ChatServer{})
	grpcServer.Serve(lis)
}
