package main

import (
	"google.golang.org/grpc"
	pb "grpc-demo/proto"
	"grpc-demo/server"
	"log"
	"net"
)

func main() {
	listen, err := net.Listen("tcp", ":3200")
	if err != nil {
		log.Fatal(err)
	}

	s := grpc.NewServer()
	pb.RegisterUsersServer(s, &server.UsersServer{})

	log.Println("RPC Service started")

	if err := s.Serve(listen); err != nil {
		log.Fatal(err)
	}
}
