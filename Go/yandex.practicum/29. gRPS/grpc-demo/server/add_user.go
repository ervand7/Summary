package server

import (
	"context"
	"fmt"
	pb "grpc-demo/proto"
)

func (s *UsersServer) AddUser(ctx context.Context, in *pb.AddUserRequest) (*pb.AddUserResponse, error) {
	var response pb.AddUserResponse

	if _, ok := s.users.Load(in.User.Email); ok {
		response.Error = fmt.Sprintf(`User with current email %s already exist`, in.User.Email)
	} else {
		s.users.Store(in.User.Email, in.User)
	}
	return &response, nil
}
