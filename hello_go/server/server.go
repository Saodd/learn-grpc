package main

import (
	"context"
	"encoding/base32"
	"fmt"
	"github.com/Saodd/learn-grpc/hello_go"
	"google.golang.org/grpc"
	"log"
	"math/rand"
	"net"
	"time"
)

var ServerName string

func makeServerName() {
	r := make([]byte, 8)
	rand.Seed(time.Now().UnixNano())
	rand.Read(r)
	ServerName = base32.StdEncoding.EncodeToString(r)
}

type ChatServer struct {
	hello_go.ChatServer
}

func (s *ChatServer) Echo(ctx context.Context, sentence *hello_go.Sentence) (*hello_go.Sentence, error) {
	fmt.Println("收到: ", sentence)
	sentence.Speaker = "Lewin-Server-" + ServerName
	return sentence, nil
}

func main() {
	makeServerName()
	lis, err := net.Listen("tcp", "0.0.0.0:5005")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	grpcServer := grpc.NewServer()
	hello_go.RegisterChatServer(grpcServer, &ChatServer{})
	grpcServer.Serve(lis)
}
