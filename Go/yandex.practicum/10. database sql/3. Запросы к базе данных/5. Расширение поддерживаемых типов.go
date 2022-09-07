package main

import (
	"database/sql/driver"
	"errors"
	"fmt"
	"strings"
)

type (
	Video_ struct {
		Id   string
		Name string
		Tags Tags
	}

	Tags []string
)

/*
Чтобы сканировать теги, реализуем интерфейсы database/driver.Valuer и
database/sql.Scanner.
Для этого нужно определить методы:
	Value() — для записи в БД и приведения данных к простому типу;
	Scan() — для чтения из БД и приведения данных к сложным типам и структурам Go.
*/

// Value — функция для тегов, которая наследуется из пакета database/sql.
func (tags Tags) Value() (driver.Value, error) {
	// преобразуем []string в string
	if len(tags) == 0 {
		return "", nil
	}
	return strings.Join(tags, "|"), nil
}

func (tags *Tags) Scan(value interface{}) error {
	// Если value — это поле nil, возвращаем пустой массив.
	if value == nil {
		*tags = Tags{}
		return nil
	}

	/*
		Функцией driver.String.ConvertValue(value) пытаемся конвертировать
		значение в строку. Если не получится, функция вернёт ошибку.
		Открыв функцию driver.String.ConvertValue(value), увидим, что
		она никогда не возвращает ошибку.
	*/
	sv, err := driver.String.ConvertValue(value)
	if err != nil {
		return fmt.Errorf("cannot scan value. %w", err)
	}

	v, ok := sv.(string)
	if !ok {
		return errors.New("cannot scan value. cannot convert value to string")
	}

	// После этого указываем, чему должен равняться атрибут tags
	*tags = strings.Split(v, "|")

	return nil
}
