package main

import (
	"fmt"
	"log"
	"net"
	"sync"
	"time"

	pb "main/proto"

	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedStreamServiceServer
}

func (s server) FetchResponse(
	in *pb.Request, srv pb.StreamService_FetchResponseServer,
) error {
	log.Printf("fetch response for id : %d", in.Id)

	// use wait group to allow process to be concurrent
	var wg sync.WaitGroup
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func(count int64) {
			defer wg.Done()

			// time sleep to simulate server process time
			time.Sleep(time.Duration(count) * time.Second)
			resp := pb.Response{
				Result: fmt.Sprintf("Request #%d For Id:%d", count, in.Id),
			}
			if err := srv.Send(&resp); err != nil {
				log.Printf("send error %v", err)
			}
			log.Printf("finishing request number : %d", count)
		}(5)
	}

	wg.Wait()
	return nil
}

func main() {
	// create listiner
	lis, err := net.Listen("tcp", ":50005")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	// create grpc server
	s := grpc.NewServer()
	pb.RegisterStreamServiceServer(s, server{})

	log.Println("start server")
	// and start...
	if err = s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
