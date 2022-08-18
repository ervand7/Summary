package main

import (
	"encoding/hex"
	"encoding/json"
	"fmt"
)

/* ОЧЕНЬ ВАЖНО!!! Если у типа определены методы MarshalJSON и UnmarshalJSON,
и при этом тип является вложенным, то при глобальном
MarshalJSON, UnmarshalJSON над объектом, содержащим этт вложенный тип,
применится его кастомный MarshalJSON и UnmarshalJSON.
*/

/*
Нужно сделать так, чтобы тип []byte в JSON-представлении был
в виде шестнадцатеричной строки.

Вставьте недостающий код в программу, чтобы она выводила:
{"ID":7,"Slice":"0102030a0bff"}
{7 [1 2 3 10 11 255]}
*/

type Slice []byte

// MarshalJSON реализует интерфейс json.Marshaler.
func (s Slice) MarshalJSON() ([]byte, error) {
	return json.Marshal(hex.EncodeToString(s))
}

// UnmarshalJSON реализует интерфейс json.Unmarshaler.
func (s *Slice) UnmarshalJSON(data []byte) error {
	var tmp string
	if err := json.Unmarshal(data, &tmp); err != nil {
		return err
	}
	v, err := hex.DecodeString(tmp)
	if err != nil {
		panic(err)
	}
	*s = v
	return err
}

type MySlice struct {
	ID    int
	Slice Slice
}

func main() {
	ret, err := json.Marshal(
		MySlice{
			ID: 7,
			Slice: []byte{
				1, 2, 3, 10, 11, 255,
			},
		},
	)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(ret)) // {"ID":7,"Slice":"0102030a0bff"}

	var result MySlice
	if err = json.Unmarshal(ret, &result); err != nil {
		panic(err)
	}
	fmt.Println(result) // {7 [1 2 3 10 11 255]}
}
