package main

import (
	"encoding/json"
	"fmt"
	"log"
)

/*
Опишите структуру Data так, чтобы программа
вывела [{"name":"John Doe"},{"name":"Вася","comp":"Яндекс"}]
*/

type Data struct {
	ID      int    `json:"-"`
	Name    string `json:"name"`
	Company string `json:"comp,omitempty"`
}

func main() {
	foo := []Data{
		{
			ID:   10,
			Name: "John Doe",
		},
		{
			Name:    "Вася",
			Company: "Яндекс",
		},
	}
	out, err := json.Marshal(foo)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(out))
}

// [{"name":"John Doe"},{"name":"Вася","comp":"Яндекс"}]
