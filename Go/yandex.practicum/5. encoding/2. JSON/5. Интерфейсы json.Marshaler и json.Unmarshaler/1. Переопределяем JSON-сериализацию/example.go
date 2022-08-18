package main

import (
	"encoding/json"
	"fmt"
	"time"
)

// Время будет представлено в виде числа.

type Transaction struct {
	SequenceId  int `json:"-"`
	BlockNumber int `json:"block_number,omitempty"`
	Hash        string
	Parent      *Transaction `json:"parent,omitempty"`
	ExtData     []byte       `json:"ext_data,omitempty"`
	CreatedAt   time.Time    `json:"created_at"` // это поле будет переопределено
	receivedAt  time.Time
}

// MarshalJSON реализует интерфейс json.Marshaler
func (t Transaction) MarshalJSON() ([]byte, error) {
	// чтобы избежать рекурсии при json.Marshal, объявляем новый тип
	type TransactionAlias Transaction

	aliasValue := struct {
		TransactionAlias
		// переопределяем поле внутри анонимной структуры
		CreatedAt int64 `json:"created_at"`
	}{
		// встраиваем значение всех полей изначального объекта (embedding)
		TransactionAlias: TransactionAlias(t),
		// задаём значение для переопределённого поля
		CreatedAt: t.CreatedAt.Unix(),
	}

	return json.Marshal(aliasValue) // вызываем стандартный Marshal
}

// UnmarshalJSON реализует интерфейс json.Unmarshaler.
func (t *Transaction) UnmarshalJSON(data []byte) error {
	// чтобы избежать рекурсии при json.Unmarshal, объявляем новый тип
	type TransactionAlias Transaction

	aliasValue := &struct {
		*TransactionAlias
		// переопределяем поле внутри анонимной структуры
		CreatedAt int64 `json:"created_at"`
	}{
		// задаём указатель на целевой объект
		TransactionAlias: (*TransactionAlias)(t),
	}

	// вызываем стандартный Unmarshal
	if err := json.Unmarshal(data, aliasValue); err != nil {
		return err
	}
	// вручную задаём значение поля time.Time
	t.CreatedAt = time.Unix(aliasValue.CreatedAt, 0)

	return nil
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
	txBz, err := tx.MarshalJSON()
	if err != nil {
		panic(err)
	}
	marshaled := string(txBz)
	fmt.Println(marshaled)
	/*
		{
			"block_number":1,
			"Hash":"0102AABB",
			"parent":{
				"Hash":"0102AABA",
				"created_at":1660766581
			},
			"ext_data":"AQID",
			"created_at":1660766582
		}
	*/

	unmarshaled := Transaction{}
	unmarshaled.UnmarshalJSON([]byte(marshaled))
	fmt.Printf("%+#v", unmarshaled)
	/*
		&main.Transaction{
		SequenceId:0,
		BlockNumber:1,
		Hash:"0102AABB",
		Parent:(*main.Transaction)(0x140001321c0),  // через debugger parent видно
		ExtData:[]uint8{0x1, 0x2, 0x3},
		CreatedAt:time.Date(2022, time.August, 18, 8, 21, 47, 0, time.Local),
		receivedAt:time.Time{wall:0x0, ext:0, loc:(*time.Location)(nil)}
		}
	*/
}
