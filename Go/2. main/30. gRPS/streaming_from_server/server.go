package main

import (
	"fmt"
	"log"
	"net"
	"time"

	"google.golang.org/grpc"

	pb "streaming_from_server/proto"
)

type MultiServer struct {
	pb.UnimplementedStreamMultiServiceServer
}

func (s MultiServer) MultiResponse(
	in *pb.Request, srv pb.StreamMultiService_MultiResponseServer,
) error {
	fmt.Printf(
		"%s Start streaming %d * [1..%d]\n",
		time.Now().Format("15:04:05"),
		in.Num, in.Limit,
	)
	for i := int64(1); i <= int64(in.Limit); i++ {
		time.Sleep(100 * time.Millisecond)
		resp := pb.Response{Result: int64(in.Num) * i}

		if err := srv.Send(&resp); err != nil {
			log.Fatal(err)
		}
	}
	return nil
}

func main() {
	// определяем порт для сервера
	listen, err := net.Listen("tcp", ":3200")
	if err != nil {
		log.Fatal(err)
	}
	// создаём gRPC-сервер без зарегистрированной службы
	s := grpc.NewServer()
	// регистрируем сервис
	pb.RegisterStreamMultiServiceServer(s, MultiServer{})

	fmt.Println("Start gRPC server")
	if err := s.Serve(listen); err != nil {
		log.Fatal(err)
	}
}
