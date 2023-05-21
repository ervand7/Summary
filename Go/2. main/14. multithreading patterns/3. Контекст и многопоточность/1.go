package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"net/http"
	"sync"
)

func healthCheck(
	ctx context.Context, url string, errCh chan<- error, wg *sync.WaitGroup,
) {
	var defErr error
	defer func() {
		if defErr != nil {
			select {
			case errCh <- defErr:
			case <-ctx.Done():
				log.Println("aborting", url)
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
	ctx, cancel := context.WithCancel(context.Background())

	hostsToCheck := []string{
		"https://ya1ndex.ru",
		"https://eda.yandex.ru",
		"https://lavka.yan1dex.ru",
	}
	for _, hostToCheck := range hostsToCheck {
		log.Println("checking", hostToCheck)
		wg.Add(1)
		go healthCheck(ctx, hostToCheck, errCh, wg)
	}

	go func() {
		wg.Wait()
		close(errCh)
	}()

	if err := <-errCh; err != nil {
		log.Println(err)
		cancel()
		return
	}

	log.Println("successful healthcheck")
}
