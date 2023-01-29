package main

import (
	"context"
	"fmt"
	"log"

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
		if resp, err := c.GetUser(context.Background(), &pb.GetUserRequest{
			Email: userEmail,
		}); err != nil {
			log.Fatal(err)
		} else if resp.Error == "" {
			fmt.Println(resp.User)
		} else {
			fmt.Println(resp.Error)
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
