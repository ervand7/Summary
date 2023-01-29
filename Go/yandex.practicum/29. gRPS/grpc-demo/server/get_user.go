package server

import (
	"context"
	"fmt"
	pb "grpc-demo/proto"
)

func (s *UsersServer) GetUser(ctx context.Context, in *pb.GetUserRequest) (*pb.GetUserResponse, error) {
	var response pb.GetUserResponse

	user, ok := s.users.Load(in.Email)
	if !ok {
		response.Error = fmt.Sprintf(`User with email %s doesn't exist`, in.Email)
		return &response, nil
	}

	response.User = user.(*pb.User)
	return &response, nil
}
