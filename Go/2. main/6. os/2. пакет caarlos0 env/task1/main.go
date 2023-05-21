package main

import (
	"fmt"
	"github.com/caarlos0/env/v6"
	"log"
)

// Выведите имя текущего пользователя в консоль с помощью пакета caarlos0/env.

type Config struct {
	User string `env:"USER"`
}

func main() {
	var cfg Config
	err := env.Parse(&cfg)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Current user is %s\n", cfg.User)
}
