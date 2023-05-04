package main

import (
	"log"
	"net/http"
	"strconv"
)

// GET http://localhost:8080/?url=https://yandex.ru&num=10

const workersMaxCount int = 10

func makeRequest(url string) {
	log.Println("making request to", url)

	_, err := http.Get(url)
	if err != nil {
		log.Println(err)
		return
	}

	log.Println("success", url)
}

func main() {
	urlsChan := make(chan string)
	// Одновременно сможем ддосить workersMaxCount раз. Потому что у нас
	// будет всего workersMaxCount горутин
	for i := 0; i < workersMaxCount; i++ {
		go func() {
			for url := range urlsChan {
				makeRequest(url)
			}
		}()
	}

	// это DDoS-прокси
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		url := r.FormValue("url")
		reqsCountRaw := r.FormValue("num")
		reqsCount, err := strconv.Atoi(reqsCountRaw)
		if err != nil {
			http.Error(w, "wrong number", http.StatusBadRequest)
			return
		}

		for i := 0; i < reqsCount; i++ {
			urlsChan <- url
		}

		w.WriteHeader(http.StatusOK)
	})

	http.ListenAndServe(":8080", nil)
}
