package main

import (
	"context"
	"fmt"
	"github.com/Saodd/learn-grpc/hello_go"
	"google.golang.org/grpc"
	"log"
)

func main() {
	// 1. 建立连接。这里可以配置很多选项，例如 TLS, JWT 等
	var opts = []grpc.DialOption{
		grpc.WithInsecure(), // 本地不安全连接必须指定这个
	}
	conn, err := grpc.Dial("localhost:5005", opts...)
	if err != nil {
		log.Fatal("连接失败: ", err)
	}
	defer conn.Close()

	// 2. 实例化一个专用客户端对象
	client := hello_go.NewChatClient(conn)
	// 3. 执行调用
	req := hello_go.Sentence{
		Speaker: "Lewin-Client",
		Content: "Hello, world!",
	}
	resp, err := client.Echo(context.Background(), &req)
	if err != nil {
		log.Fatalln("调用失败: ", err)
	}
	fmt.Println("收到回复: ", resp)
}
