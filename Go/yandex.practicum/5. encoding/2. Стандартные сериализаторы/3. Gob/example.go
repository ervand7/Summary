package main

import (
	"bytes"
	"encoding/gob"
	"fmt"
)

// SendData — структура для кодирования.
type SendData struct {
	Value   int
	Balance *float64
	Name    string
	private int
}

// GetData — структура для декодирования.
type GetData struct {
	Name    string
	Balance float64
	Ext     []byte
	value   int
}

func main() {
	// создаём исходный объект
	floatValue := 50.0
	data := SendData{
		Value:   100,
		Balance: &floatValue,
		Name:    "some_string",
		private: 1,
	}
	// создаём хранилище байт и энкодер/декодер
	var buffer bytes.Buffer
	// кодирование
	if err := gob.NewEncoder(&buffer).Encode(data); err != nil {
		panic(err)
	}

	// сейчас buffer содержит data в формате gob
	// декодирование будет в переменную типа GetData
	var out GetData
	if err := gob.NewDecoder(&buffer).Decode(&out); err != nil {
		panic(err)
	}
	fmt.Printf("out: %+v\n", out)

	// Output: {Name:some_string Balance:50 Ext:[] value:0}

	// eсли определить var out SendData, то результат будет примерно таким:
	// {Value:100 Balance:0xc000018418 Name:some_string private:0}
}
