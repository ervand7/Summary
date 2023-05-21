package main

import (
	"errors"
	"fmt"
	"os"
	"time"
)

// TimeError Создадим собственный тип, который удовлетворяет интерфейсу error
type TimeError struct {
	Time time.Time
	Text string
}

func (t TimeError) Error() string {
	return fmt.Sprintf(
		"%v: %v",
		t.Time.Format(
			`2006/01/02 15:04:05`,
		),
		t.Text,
	)
}

// NewTimeError возвращает переменную типа TimeError c текущим временем.
func NewTimeError(text string) TimeError {
	return TimeError{
		Time: time.Now(),
		Text: text,
	}
}

func testFunc(i int) error {
	// несмотря на то, что NewTimeError возвращает тип TimeError,
	// у testFunc тип возвращаемого значения равен error
	if i == 0 {
		return NewTimeError(`параметр в testFunc равен 0`)
	}
	return nil
}

func main() {
	if err := testFunc(0); err != nil {
		fmt.Println(err)
	}

	// type assertion without switch
	if err := testFunc(0); err != nil {
		if v, ok := err.(TimeError); ok {
			fmt.Println(v.Time, v.Text)
		} else {
			fmt.Println(err)
		}
	}

	// type assertion with switch
	if err := testFunc(0); err != nil {
		switch v := err.(type) {
		case TimeError:
			fmt.Println(v.Time, v.Text)
		case *os.PathError:
			fmt.Println(v.Err)
		default:
			fmt.Println(err)
		}
	}

	// errors.As
	if err := testFunc(0); err != nil {
		var t TimeError
		// Сравниваем полученную и контрольную ошибки. Сравнение идёт по типу ошибки.
		if ok := errors.As(err, &t); ok {
			fmt.Println(t.Time, t.Text)
		} else {
			fmt.Println(err)
		}
	}
}
