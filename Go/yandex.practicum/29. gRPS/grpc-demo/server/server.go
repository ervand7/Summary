package server

import (
	pb "grpc-demo/proto"
	"sync"
)

type UsersServer struct {
	pb.UnimplementedUsersServer
	users sync.Map
}