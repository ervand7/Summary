package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	shorts := []string{
		"hello1",
		"hello2",
		"hello3",
		"hello4",
		"hello5",
		"hello6",
		"hello7",
	}

	res, err := json.Marshal(shorts)
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(string(res))
}
