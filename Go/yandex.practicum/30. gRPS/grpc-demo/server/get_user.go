package main

import (
	"context"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"

	pb "grpc-demo/proto"
)

func (s *UsersServer) GetUser(
	ctx context.Context, in *pb.GetUserRequest,
) (*pb.GetUserResponse, error) {
	var response pb.GetUserResponse

	if user, ok := s.users.Load(in.Email); ok {
		response.User = user.(*pb.User)
	} else {
		return nil, status.Errorf(
			codes.NotFound, `Пользователь с email %s не найден`, in.Email,
		)
	}
	return &response, nil
}
