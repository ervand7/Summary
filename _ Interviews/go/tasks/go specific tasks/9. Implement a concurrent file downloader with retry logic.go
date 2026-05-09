package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

func DownloadFile(ctx context.Context, url string) (string, error) {
	select {
	case <-time.After(100 * time.Millisecond):

		// simulate flaky download
		if len(url)%4 == 0 {
			return "", errors.New("temporary download error")
		}

		return "content-of-" + url, nil

	case <-ctx.Done():
		return "", ctx.Err()
	}
}

func DownloadAll(
	ctx context.Context,
	urls []string,
	workers int,
	maxRetries int,
) (map[string]string, error) {
	/*
		Requirements:
		- concurrent downloads
		- max workers parallel downloads
		- retry failed downloads up to maxRetries
		- collect successful downloads
		- return partial results if needed
		- respect context cancellation
		- no goroutine leaks
		- return first error if any
	*/
	result := make(map[string]string)

	if len(urls) == 0 {
		return result, nil
	}

	if workers <= 0 {
		return nil, errors.New("workers count should be positive")
	}

	if maxRetries <= 0 {
		return nil, errors.New("maxRetries count should be positive")
	}

	var (
		firstErr error
		mu       sync.Mutex
		wg       sync.WaitGroup
		urlsCh   = make(chan string)
	)

	for i := 0; i < workers; i++ {
		wg.Add(1)

		go func() {
			defer wg.Done()

			for {
				select {
				case <-ctx.Done():
					return

				case url, ok := <-urlsCh:
					if !ok {
						return
					}

					var (
						content string
						err     error
					)

				stopRetries:
					for r := 0; r < maxRetries; r++ {
						select {
						case <-ctx.Done():
							return
						default:
							content, err = DownloadFile(ctx, url)
							if err == nil {
								break stopRetries
							}
						}
					}

					select {
					case <-ctx.Done():
						return
					default:
						mu.Lock()
						if err != nil {
							if firstErr == nil {
								firstErr = err
							}
						} else {
							result[url] = content
						}
						mu.Unlock()
					}
				}
			}
		}()
	}

stopProduce:
	for _, url := range urls {
		select {
		case <-ctx.Done():
			break stopProduce
		case urlsCh <- url:
		}
	}

	close(urlsCh)
	wg.Wait()

	if firstErr != nil {
		return result, firstErr
	}

	if ctx.Err() != nil {
		return result, ctx.Err()
	}

	return result, nil
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
	defer cancel()

	urls := []string{
		"url1",
		"url2",
		"url3333",
		"url4444",
		"url5",
		"url6666",
	}

	results, err := DownloadAll(ctx, urls, 3, 3)

	fmt.Println("error:", err)
	fmt.Println("downloaded:", len(results))

	for url, content := range results {
		fmt.Println(url, content)
	}
}
