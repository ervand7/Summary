package httpttest

import (
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/status", StatusHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
