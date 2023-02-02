package main

import (
	"context"
	"fmt"
	"log"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"

	pb "grpc-demo/proto"
)

func TestUsers(c pb.UsersClient) {
	users := []*pb.User{
		{Name: `John`, Email: `john@example.com`, Sex: pb.User_MAN},
		{Name: `Alice`, Email: `alice@example.com`, Sex: pb.User_WOMAN},
		{Name: `Max`, Email: `max@example.com`, Sex: pb.User_MAN},

		{Name: `Alice`, Email: `alice@example.com`, Sex: pb.User_WOMAN},
	}
	for _, user := range users {
		resp, err := c.AddUser(context.Background(), &pb.AddUserRequest{
			User: user,
		})
		if err != nil {
			log.Fatal(err)
		}
		if resp.Error != "" {
			fmt.Println(resp.Error)
		}
	}

	if resp, err := c.DelUser(context.Background(), &pb.DelUserRequest{
		Email: `john@example.com`,
	}); err != nil {
		log.Fatal(err)
	} else if resp.Error != "" {
		fmt.Println(resp.Error)
	}

	for _, userEmail := range []string{`john@example.com`, `alice@example.com`} {
		_, err := c.GetUser(context.Background(), &pb.GetUserRequest{
			Email: userEmail,
		})
		if err != nil {
			if e, ok := status.FromError(err); ok {
				if e.Code() == codes.NotFound {
					// выведет, что пользователь не найден
					fmt.Println(`NOT FOUND`, e.Message())
				} else {
					// в остальных случаях выводим код ошибки в виде строки и сообщение
					fmt.Println(e.Code(), e.Message())
				}
			} else {
				fmt.Printf("Не получилось распарсить ошибку %v", err)
			}
		}
	}

	emails, err := c.ListUsers(context.Background(), &pb.ListUsersRequest{
		Offset: 0,
		Limit:  100,
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(emails.Count, emails.Emails)
}
