package main

import (
	"context"
	"io"
	"log"
	"math/rand"
	"sync"
	"testing"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"

	pb "streaming_from_server/proto"
)

func TestMultiServer(t *testing.T) {
	// устанавливаем соединение с сервером
	conn, err := grpc.Dial(
		":3200",
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	)
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	// создаём клиент для чтения потока
	client := pb.NewStreamMultiServiceClient(conn)

	rand.Seed(time.Now().UnixNano())
	tests := []struct {
		num   int32
		limit int32
	}{
		{18, 12},
		{100, 7},
		{25, 10},
		// дополнительно проверяем для случайных чисел
		{rand.Int31(), rand.Int31n(50)},
		{rand.Int31(), rand.Int31n(50)},
		{rand.Int31(), rand.Int31n(50)},
	}

	var wg sync.WaitGroup

	// функция, которая возвращает ожидаемый результат тестового стрима
	want := func(initial, limit int32) (result int64) {
		for i := int64(1); i <= int64(limit); i++ {
			result += int64(initial) * i
		}
		return
	}

	for i := range tests {
		wg.Add(1)
		go func(i int) {
			stream, err := client.MultiResponse(
				context.Background(),
				&pb.Request{Num: tests[i].num, Limit: tests[i].limit},
			)
			if err != nil {
				log.Fatal(err)
			}
			var get int64
			for {
				resp, err := stream.Recv()
				if err == io.EOF {
					wg.Done()
					break
				}
				if err != nil {
					log.Fatal(err)
				}
				get += resp.Result
			}
			if want := want(tests[i].num, tests[i].limit); get != want {
				t.Errorf(
					`%d * [1..%d] ожидается %d получено %d`,
					tests[i].num,
					tests[i].limit,
					want,
					get,
				)
			}
		}(i)
	}
	wg.Wait()
}
