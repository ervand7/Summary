package main

import (
	"sync"

	pb "grpc-demo/proto"
)

// UsersServer поддерживает все необходимые методы сервера
type UsersServer struct {
	// нужно встраивать тип pb.Unimplemented<TypeName>
	// для совместимости с будущими версиями
	pb.UnimplementedUsersServer

	// используем sync.Map для хранения пользователей
	users sync.Map
}
