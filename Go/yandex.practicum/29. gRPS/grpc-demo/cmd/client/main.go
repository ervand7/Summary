package main

import (
	"google.golang.org/grpc"
	pb "grpc-demo/proto"
	"log"
)

func main() {
	conn, err := grpc.Dial(`:3200`, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	c := pb.NewUsersClient(conn)

	TestUsers(c)
}
