package main

import (
	"fmt"
	"sync"
	"time"
)

/*
На примере хорошо видно, что если нет записи, читать одновременно могут все
горутины. Однако, как только начинается запись, чтение для всех остальных
горутин заблокировано.
*/

var data []string
var rwMutex sync.RWMutex

func writer(i int) {
	rwMutex.Lock()
	{
		fmt.Println("****> : Performing Write. No one can read!\n")
		time.Sleep(time.Second)
		data = append(data, fmt.Sprintf("String: %d", i))
	}
	rwMutex.Unlock()
}

func reader(id int) {
	rwMutex.RLock()
	{
		fmt.Printf("%d : Performing Read : Length[%d]\n", id, len(data))
	}
	rwMutex.RUnlock()
}

func main() {
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		for i := 0; i < 10; i++ {
			writer(i)
		}
		wg.Done()
	}()
	for i := 0; i < 100; i++ {
		go func(id int) {
			for {
				reader(id)
			}
		}(i)
	}
	wg.Wait()
	fmt.Println("Program Complete")
}
