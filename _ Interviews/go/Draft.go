package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	ch := make(chan []byte)
	go func(recv chan []byte) {
		resp, _ := http.Get("https://example.com")
		defer resp.Body.Close()
		jsonBytes, _ := ioutil.ReadAll(resp.Body)
		recv <- jsonBytes
	}(ch)

	fmt.Println("Program continues...")
	// Do other things

	// Then wait for HTTP response to come back
	result := <-ch
	fmt.Println("Done, result is", string(result))
}
