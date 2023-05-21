package main

import (
	"fmt"
	"reflect"
)

// Напишите метод клонирования объекта указанного типа

type Config struct {
	Version string
	Plugins []string
	Stat    map[string]int
}

func (cfg *Config) Clone() *Config {
	clone := new(Config)
	clone.Version = cfg.Version
	clone.Stat = make(map[string]int)
	for k, v := range cfg.Stat {
		clone.Stat[k] = v
	}
	for _, v := range cfg.Plugins {
		clone.Plugins = append(clone.Plugins, v)
	}

	return clone
}

func main() {
	cfg := &Config{
		Version: "v0.1",
		Stat: map[string]int{
			"hello": 123,
			"world": 234,
		},
		Plugins: []string{"q", "w", "e", "r", "t", "y"},
	}

	clone := cfg.Clone()
	fmt.Println(reflect.DeepEqual(cfg, clone))
}
