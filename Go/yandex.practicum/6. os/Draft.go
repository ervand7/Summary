package main

import (
	"encoding/json"
	"fmt"
)

type URLMap struct {
	URLPair map[string]string `json:"url"`
}

func main() {
	urlMap := URLMap{
		URLPair: make(map[string]string, 0),
	}
	urlMap.URLPair["hello"] = "world"
	result, _ := json.Marshal(urlMap)
	fmt.Println(string(result))
}
