package main

import (
	"fmt"
	"sync"
	"time"
)

/*
Но о закрытии канала можно оповестить только один раз (см. предыдущий пример).
А sync.Cond стандартной библиотеки Go позволяет много раз отправлять
подписчикам уведомления. Эта конструкция также может защитить мьютексом
общий для подписчиков ресурс.
*/

type subscriber struct {
	ID int
}

// Subscribe ожидает уведомления.
func (s subscriber) Subscribe(c *sync.Cond) {
	for {
		c.L.Lock()
		c.Wait()
		fmt.Printf("subscriber %v is notified\n", s.ID)
		c.L.Unlock()
	}
}

func main() {
	cond := sync.NewCond(new(sync.Mutex))
	s1 := subscriber{1}
	go s1.Subscribe(cond)
	s2 := subscriber{2}
	go s2.Subscribe(cond)
	s3 := subscriber{3}
	go s3.Subscribe(cond)
	time.Sleep(1 * time.Second)
	// отправка уведомлений всем подписчикам
	cond.Broadcast()
	time.Sleep(1 * time.Second)
	fmt.Println("Once more")
	cond.Broadcast()
	time.Sleep(1 * time.Second)
}

/*
subscriber 1 is notified
subscriber 2 is notified
subscriber 3 is notified
Once more
subscriber 3 is notified
subscriber 1 is notified
subscriber 2 is notified
*/
