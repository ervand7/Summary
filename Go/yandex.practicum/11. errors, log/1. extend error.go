package main

import (
	"fmt"
	"time"
)

/*
При создании ошибок всегда нужно возвращать указатели на структуру.
Тогда, если создать ошибки с одинаковыми данными, они не будут равны друг другу.
Например, если создать ошибку errors.New("EOF"), она не будет равна io.EOF,
которая определяется точно так же. Если вместо указателя возвращать структуру,
то нельзя будет однозначно идентифицировать ошибку.
*/

// TimeError предназначен для ошибок с фиксацией времени возникновения.
type TimeError struct {
	Time time.Time
	Err  error
}

// Error добавляет поддержку интерфейса error для типа TimeError.
func (te *TimeError) Error() string {
	return fmt.Sprintf("%v %v", te.Time.Format(`2006/01/02 15:04:05`), te.Err)
}

// NewTimeError упаковывает ошибку err в тип TimeError c текущим временем.
func NewTimeError(err error) error {
	return &TimeError{
		Time: time.Now(),
		Err:  err,
	}
}

// Unwrap реализуем дополнительно
func (te *TimeError) Unwrap() error {
	return te.Err
}
