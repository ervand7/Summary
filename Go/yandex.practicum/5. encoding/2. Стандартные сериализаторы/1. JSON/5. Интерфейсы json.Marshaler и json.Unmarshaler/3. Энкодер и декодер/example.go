package main

import (
	"bytes"
	"encoding/json"
)

type MyType struct {
	// Type задаёт тип объекта поля Value
	Type int `json:"type"`
	// Value содержит объект типа {TypeA, TypeB}
	Value interface{} `json:"value"` // json.Unmarshal десериализует тип interface{} в map[string]interface{}
}

func main() {
	var buf bytes.Buffer
	jsonDecoder := json.NewDecoder(&buf)
	jsonEncoder := json.NewEncoder(&buf)

	var v MyType
	jsonDecoder.Decode(&v)
	jsonEncoder.Encode(v)
}
