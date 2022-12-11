package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

const IDLength = 6

var Alphabet = []rune("0123456789abcdefghijklmnopqrstuvwxyz")

func GenerateName() string {
	name := make([]rune, IDLength)
	for i := 0; i < IDLength; i++ {
		name[i] = Alphabet[rand.Intn(len(Alphabet))]
	}
	return string(name)
}

type Generator struct {
	Names map[string]struct{}
	Mutex sync.Mutex
}

func NewGenerator() *Generator {
	return &Generator{
		Names: make(map[string]struct{}),
	}
}

func (gen *Generator) GetUniqueName() string {
	for {
		name := GenerateName()
		gen.Mutex.Lock()
		if _, ok := gen.Names[name]; !ok {
			gen.Names[name] = struct{}{}
			gen.Mutex.Unlock()
			return name
		}
		gen.Mutex.Unlock()
	}
}

func main() {
	gen := NewGenerator()
	for i := 0; i < 5; i++ {
		go func() {
			for j := 0; j < 10; j++ {
				fmt.Println(gen.GetUniqueName())
			}
		}()
	}
	time.Sleep(1 * time.Second)
}
