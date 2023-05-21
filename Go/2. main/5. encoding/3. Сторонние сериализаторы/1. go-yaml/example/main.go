package main

import (
	"fmt"
	"gopkg.in/yaml.v3"
	"time"
)

type (
	AccountBalance struct {
		AccountIdHash []byte           `yaml:"account_id_hash,flow"`
		Amounts       []CurrencyAmount `yaml:"amounts,omitempty"`
		IsBlocked     bool             `yaml:"is_blocked"`
		UpdatedAt     time.Time        `yaml:"updated_at"`
	}

	CurrencyAmount struct {
		Amount   int64  `yaml:"amount"`
		Decimals int8   `yaml:"decimals"`
		Symbol   string `yaml:"symbol"`
	}
)

func main() {
	balance := AccountBalance{
		AccountIdHash: []byte{0x10, 0x20, 0x0A, 0x0B},
		Amounts: []CurrencyAmount{
			{Amount: 1000000, Decimals: 2, Symbol: "RUB"},
			{Amount: 2510, Decimals: 2, Symbol: "USD"},
		},
		IsBlocked: true,
		UpdatedAt: time.Date(2021, time.January, 10, 15, 20, 0, 0, time.UTC),
	}

	// преобразуем значение переменной balance в YAML-формат
	out, err := yaml.Marshal(balance)
	if err != nil {
		panic(err)
	}
	fmt.Println(string(out))
}

/*
account_id_hash: [16, 32, 10, 11]
amounts:
- amount: 1000000
  decimals: 2
  symbol: RUB
- amount: 2510
  decimals: 2
  symbol: USD
is_blocked: true
updated_at: 2021-01-10T15:20:00Z
*/
