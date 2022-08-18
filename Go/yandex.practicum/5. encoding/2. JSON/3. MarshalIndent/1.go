package main

import (
	"encoding/json"
	"fmt"
	"time"
)

type Transaction struct {
	SequenceId  int `json:"-"`
	BlockNumber int `json:"block_number,omitempty"`
	Hash        string
	Parent      *Transaction `json:"parent,omitempty"`
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
	txBz, err := json.MarshalIndent(tx, "", "  ")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(txBz))
}

/*
{
  "block_number": 1,
  "Hash": "0102AABB",
  "parent": {
    "Hash": "0102AABA",
    "created_at": "2022-08-17T19:13:48.481806Z"
  },
  "ext_data": "AQID",
  "created_at": "2022-08-17T19:13:49.481806Z"
}
*/
