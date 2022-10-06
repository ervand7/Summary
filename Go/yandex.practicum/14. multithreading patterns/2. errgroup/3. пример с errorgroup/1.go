package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"net/http"

	"golang.org/x/sync/errgroup"
)

func main() {
	g, _ := errgroup.WithContext(context.Background())

	hostsToCheck := []string{
		"https://yandex.ru",
		"https://eda.yandex.ru",
		"https://lavka.yandex.ru",
	}
	for _, hostToCheck := range hostsToCheck {
		log.Println("checking", hostToCheck)

		// тело функции healthCheck вставлено анонимной функцией для компактности
		hostToCheck := hostToCheck
		g.Go(func() error {
			resp, err := http.Get(hostToCheck)
			if err != nil {
				return fmt.Errorf("healthcheck failed: %w", err)
			}
			if resp.StatusCode != http.StatusOK {
				fmt.Println(resp.StatusCode)
				return errors.New("healthcheck failed: status not ok")
			}

			return nil
		})
	}

	if err := g.Wait(); err != nil {
		log.Println(err)
		return
	}

	log.Println("successful healthcheck")
}
