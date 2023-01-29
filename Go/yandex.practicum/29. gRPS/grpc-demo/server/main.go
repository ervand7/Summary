package main

import (
	"log"
	"net"

	"google.golang.org/grpc"

	pb "grpc-demo/proto"
)

func main() {
	// определяем порт для сервера
	listen, err := net.Listen("tcp", ":3200")
	if err != nil {
		log.Fatal(err)
	}

	// создаём gRPC-сервер без зарегистрированной службы
	s := grpc.NewServer()
	// регистрируем сервис
	pb.RegisterUsersServer(s, &UsersServer{})

	log.Println("RPC Service started")

	// получаем запрос gRPC
	if err := s.Serve(listen); err != nil {
		log.Fatal(err)
	}
}
