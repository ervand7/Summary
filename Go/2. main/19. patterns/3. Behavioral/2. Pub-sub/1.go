package main

import (
	"context"
	"fmt"
	"time"
)

/*
Go, как многопоточный язык, предоставляет уникальные синтаксические
возможности в конкурентном программировании. Так, реализовать паттерн
Наблюдатель можно простым закрытием канала. Завершение context.Context
стандартной библиотеки означает закрытие канала Context.Done, о чём узнают
все подписчики контекста.
*/

const shortDuration = 1 * time.Millisecond

type Subscriber struct {
	ID int
}

func (s Subscriber) Subscribe(ctx context.Context) {
	<-ctx.Done()
	fmt.Printf("Subscriber %v is notified\n", s.ID)
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), shortDuration)
	defer cancel()
	// создаём подписчиков
	s1 := Subscriber{1}
	go s1.Subscribe(ctx)
	s2 := Subscriber{2}
	go s2.Subscribe(ctx)
	s3 := Subscriber{3}
	go s3.Subscribe(ctx)
	time.Sleep(2 * time.Millisecond)
}

/*
Их порядок может меняться:
Subscriber 1 is notified
Subscriber 2 is notified
Subscriber 3 is notified
*/
