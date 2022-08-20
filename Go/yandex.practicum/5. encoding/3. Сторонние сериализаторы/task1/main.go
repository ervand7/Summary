package main

import (
	"fmt"
	"github.com/pelletier/go-toml/v2"
	"gopkg.in/yaml.v3"
)

type Data struct {
	ID     int    `toml:"id"`
	Name   string `toml:"name"`
	Values []byte `toml:"values"`
}

const yamlData = `
id: 101
name: John Doe
values:
- 11
- 22
- 33
`

func main() {
	data := Data{}
	err := yaml.Unmarshal([]byte(yamlData), &data)
	if err != nil {
		panic(err)
	}
	out, err := toml.Marshal(data)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(out))

	/*
		id = 101
		name = 'John Doe'
		values = [11, 22, 33]

	*/
}
