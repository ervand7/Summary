package main

import (
	"context"
	"io"
	"log"
	"net/http"

	"golang.org/x/sync/errgroup"
)

func fetchURL(url string) (string, error) {
	resp, err := http.Get(url)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()
	body, _ := io.ReadAll(resp.Body)
	return string(body), nil
}

func main() {
	g, ctx := errgroup.WithContext(context.Background())

	urls := []string{
		"https://example.com",
		"https://example.org",
		"https://example.net11111",
	}

	results := make([]string, len(urls))

	for i, url := range urls {
		i, url := i, url // Capture for closure

		g.Go(func() error {
			content, err := fetchURL(url)
			if err != nil {
				return err // First error cancels context
			}
			results[i] = content
			return nil
		})
	}

	if err := g.Wait(); err != nil {
		log.Fatal("Fetch failed:", err)
	}

	// Use results
	_ = ctx // ctx is cancelled if any goroutine returns error
}
