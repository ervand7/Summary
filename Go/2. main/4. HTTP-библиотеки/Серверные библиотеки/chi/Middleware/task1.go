package main

import (
	"fmt"
	"net/http"
	"time"
)

// TimerTrace замеряет время выполнения функции.
func TimerTrace(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		tStart := time.Now()
		next(w, r)
		tEnd := time.Since(tStart)
		// выводим результат в формате 7h23m0.5s
		fmt.Printf("duration for a request %s\r\n", tEnd)
	}
}
