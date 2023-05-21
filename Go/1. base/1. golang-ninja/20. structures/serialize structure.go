package main

import (
	"encoding/json"
	"fmt"
	"log"
	"time"
)

type Person_ struct {
	Name        string    `json:"Имя"`
	Email       string    `json:"Почта"`
	DateOfBirth time.Time `json:"-"` // - означает, что это поле не будет сериализовано
}

func main() {
	man := Person_{
		Name:        "Alex",
		Email:       "alex@yandex.ru",
		DateOfBirth: time.Now(),
	}
	result, err := json.Marshal(man)
	if err != nil {
		log.Fatalln("unable marshal to json")
	}
	fmt.Printf("Man %v", string(result)) // Man {"Имя":"Alex","Почта":"alex@yandex.ru"}
}
