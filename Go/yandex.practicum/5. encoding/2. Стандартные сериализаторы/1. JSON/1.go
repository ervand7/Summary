package main

import (
	"encoding/json"
	"fmt"
	"time"
)

// Transaction описывает запись блокчейна.
type Transaction struct {
	SequenceId  int `json:"-"` // Значение тега - заставляет пакет игнорировать поле
	BlockNumber int `json:"block_number,omitempty"`
	Hash        string
	Parent      *Transaction `json:"parent,omitempty"` // Наличие тега omitempty убирает JSON-ключ из представления при сериализации, если значение поля структуры не задано
	ExtData     []byte       `json:"ext_data,omitempty"`
	CreatedAt   time.Time    `json:"created_at"`
	receivedAt  time.Time
}

func main() {
	now := time.Now().UTC()

	// создаём первую запись
	parentTx := Transaction{
		SequenceId: 1,
		Hash:       "0102AABA",
		CreatedAt:  now,
		receivedAt: now.Add(10 * time.Millisecond),
	}
	// у второй записи в качестве родителя указываем parentTx
	tx := Transaction{
		SequenceId:  2,
		BlockNumber: 1,
		Hash:        "0102AABB",
		Parent:      &parentTx,
		ExtData:     []byte{1, 2, 3},
		CreatedAt:   now.Add(1 * time.Second),
		receivedAt:  now.Add(1*time.Second + 10*time.Millisecond),
	}
	// преобразуем tx в JSON-формат
	txBz, err := json.Marshal(tx)
	if err != nil {
		panic(err)
	}
	// txBz — это []byte, поэтому приводим его к типу string для печати
	fmt.Println(string(txBz))
}

/*
{
	"block_number":1,
	"Hash":"0102AABB",
	"parent":{
		"Hash":"0102AABA",
		"created_at":"2022-08-17T18:56:38.356417Z"
	},
	"ext_data":"AQID",
	"created_at":"2022-08-17T18:56:39.356417Z"
}
*/

/*
Если убрать из описания структуры все теги, консольный вывод будет таким:
{
	"SequenceId":2,
	"BlockNumber":1,
	"Hash":"0102AABB",
	"Parent":{
		"SequenceId":1,
		"BlockNumber":0,
		"Hash":"0102AABA",
		"Parent":null,
		"ExtData":null,
		"CreatedAt":"2009-11-10T23:00:00Z"
	},
	"ExtData":"AQID",
	"CreatedAt":"2009-11-10T23:00:01Z"
}
*/
