package main

import (
	"errors"
	"fmt"
	"log"
	"net/http"
)

/*
Выполнение функции в отдельной горутине усложняет обработку ошибки,
так как нельзя обработать её в месте вызова функции.
В простых случаях это не проблема, и вполне корректен такой код:
*/

func _healthCheck(uri string, errCh chan<- error) {
	resp, err := http.Get(uri)
	if err != nil {
		errCh <- fmt.Errorf("_healthCheck failed: %w", err)
		return
	}
	if resp.StatusCode != http.StatusOK {
		errCh <- errors.New("_healthCheck failed: status not ok")
		return
	}

	close(errCh)
}

func main() {
	errCh := make(chan error) // создаём канал, из которого будем ждать ошибку или nil
	for i := 0; i < 10; i++ {
		go _healthCheck("https://y1andex.ru", errCh)
	}

	err := <-errCh
	if err != nil {
		log.Println(err)
		return
	}

	log.Println("ok")
}
