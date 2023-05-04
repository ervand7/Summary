package main

import (
	"errors"
	"fmt"
	"log"
	"net/http"
	"sync"
)

func healthCheck(
	url string,
	errCh chan<- error,
	wg *sync.WaitGroup,
	stopCh <-chan struct{},
) {
	var defErr error
	defer func() {
		if defErr != nil {
			select {
			// первая горутина, поймавшая ошибку, сможет записать в канал
			case errCh <- defErr:
			// остальные завершат работу, провалившись в этот case
			case <-stopCh:
				log.Println("aborting", url)
				return
			}
		}
		wg.Done()
	}()

	resp, err := http.Get(url)
	if err != nil {
		defErr = fmt.Errorf("healthcheck failed: %w", err)
		return
	}
	if resp.StatusCode != http.StatusOK {
		defErr = errors.New("healthcheck failed: status not ok")
		return
	}
}

func main() {
	wg := &sync.WaitGroup{}
	errCh := make(chan error)
	stopCh := make(chan struct{})

	hostsToCheck := []string{
		"https://ya1ndex.ru",
		"https://eda.yandex.ru",
		"https://lavka.yan1dex.ru",
	}
	for _, hostToCheck := range hostsToCheck {
		log.Println("checking", hostToCheck)
		wg.Add(1)
		go healthCheck(hostToCheck, errCh, wg, stopCh)
	}

	// в отдельной горутине ждём завершения всех healthCheck
	// после этого закрываем канал errCh — больше записей не будет
	go func() {
		wg.Wait()
		close(errCh)
	}()

	if err := <-errCh; err != nil {
		log.Println(err)
		stopCh <- struct{}{}
		return
	}

	log.Println("successful healthcheck")
}
