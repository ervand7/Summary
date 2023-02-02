package main

import (
	"log"

	"google.golang.org/grpc"

	pb "grpc-demo/proto"
)

func main() {
	// устанавливаем соединение с сервером
	conn, err := grpc.Dial(`:3200`, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	// получаем переменную интерфейсного типа UsersClient,
	// через которую будем отправлять сообщения
	c := pb.NewUsersClient(conn)

	// функция, в которой будем отправлять сообщения
	TestUsers(c)
}
