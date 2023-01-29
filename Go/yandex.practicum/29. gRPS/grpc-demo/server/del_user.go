package server

import (
	"context"
	"fmt"
	pb "grpc-demo/proto"
)

func (s *UsersServer) DelUser(ctx context.Context, in *pb.DelUserRequest) (*pb.DelUserResponse, error) {
	var response pb.DelUserResponse

	if _, ok := s.users.LoadAndDelete(in.Email); !ok {
		response.Error = fmt.Sprintf(`User with email %s not fount`, in.Email)
	}

	return &response, nil
}
