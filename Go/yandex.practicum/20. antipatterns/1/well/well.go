package main

import (
	"fmt"
	"math/rand"
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
	Ch    chan string
}

func NewGenerator() *Generator {
	gen := &Generator{
		Names: make(map[string]struct{}),
		Ch:    make(chan string),
	}

	go gen.GenProcess()
	return gen
}

func (gen *Generator) GenProcess() {
	for {
		name := GenerateName()
		if _, ok := gen.Names[name]; !ok {
			gen.Names[name] = struct{}{}
			gen.Ch <- name
		}
	}
}

func (gen *Generator) GetUniqueName() string {
	return <-gen.Ch
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
