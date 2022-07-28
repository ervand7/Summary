package main

import (
	"context"
	"fmt"
	"time"
)

/*
В коде ниже есть два типа:
  DB — слой обращения к базе данных,
  Handler — слой бизнес-логики.
Вместо реального запроса к БД в коде стоит заглушка:
код просто ждёт секунду и отдаёт константу.

Допишите строчки кода:
Получение сигнала отмены контекста.
Отмена контекста через 500 миллисекунд.
*/

type User struct {
	Name string
}

type DB struct {
}

func (d *DB) SelectUser(ctx context.Context, email string) (User, error) {
	timer := time.NewTimer(1 * time.Second)
	select {
	case <-timer.C:
		return User{Name: "Gosha"}, nil
	case <-ctx.Done():
		return User{}, fmt.Errorf("context canceled")
	}
}

type Request struct {
	Email string
}

type Response struct {
	User User
}

type Handler struct {
	db *DB
}

func (h *Handler) HandleAPI(ctx context.Context, req Request) (Response, error) {
	u, err := h.db.SelectUser(ctx, req.Email)
	if err != nil {
		return Response{}, err
	}

	return Response{User: u}, nil
}

func main() {
	db := DB{}
	handler := Handler{db: &db}
	ctx, cancel := context.WithCancel(context.Background())

	// Отменяем контекст через какое-то время.
	// Когда запустите код и он отработает успешно,
	// попробуйте заменить длительность на 2000 миллисекунд
	time.AfterFunc(500*time.Millisecond, cancel)

	req := Request{Email: "test@yandex.ru"}
	resp, err := handler.HandleAPI(ctx, req)

	fmt.Println(resp, err)
}
