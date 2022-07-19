package main

import (
	"errors"
)

// DeliveryState — статус доставки и обработки сообщения.
type DeliveryState string

// Возможные значения перечисления DeliveryState.
const (
	DeliveryStatePending   DeliveryState = "pending"      // сообщение отправлено
	DeliveryStateAck       DeliveryState = "acknowledged" // сообщение получено
	DeliveryStateProcessed DeliveryState = "processed"    // сообщение обработано успешно
	DeliveryStateCanceled  DeliveryState = "canceled"     // обработка сообщения прервана
)

// IsValid проверяет валидность текущего значения типа DeliveryState.
func (s DeliveryState) IsValid() bool {
	switch s {
	case DeliveryStatePending, DeliveryStateAck, DeliveryStateProcessed, DeliveryStateCanceled:
		return true
	default:
		return false
	}
}

// String возвращает строковое представление типа DeliveryState.
func (s DeliveryState) String() string {
	return string(s)
}

func HandleMsgDeliveryStatus(status DeliveryState) error {
	// проверка корректности enum-значения через вызов метода типа DeliveryState
	if !status.IsValid() {
		return errors.New("status: invalid")
	}

	// код обработки сообщения

	return nil
}

func main() {
	// приводим строку "fake" к типу DeliveryState
	if err := HandleMsgDeliveryStatus(DeliveryState("fake")); err != nil {
		panic(err)
	}
}
