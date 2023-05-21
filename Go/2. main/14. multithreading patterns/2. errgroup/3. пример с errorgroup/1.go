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
	// второе возвращаемое значение — это дочерний контекст, который будет отменён
	// при первой ошибке, возвращённой обработчиками, или при завершении g.Wait()
	//
	// так вы можете получать сигнал об остановке в своём коде,
	// но в данном примере контекст не используется

	hostsToCheck := []string{
		"https://ya1ndex.ru",
		"https://eda.yandex.ru",
		"https://lavka.yan1dex.ru",
	}
	for _, hostToCheck := range hostsToCheck {
		log.Println("checking", hostToCheck)

		// тело функции healthCheck вставлено анонимной функцией для компактности
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
