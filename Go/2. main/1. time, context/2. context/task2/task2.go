package main

import (
	"context"
	"fmt"
	"time"
)

/*
Добавьте к предыдущему примеру тайм-аут. Допишите строчку кода:
Создание контекста с тайм-аутом.
*/

const (
	cancelDuration  = 2000 * time.Millisecond
	timeoutDuration = 500 * time.Millisecond
)

type Config struct {
	SelectTimeout time.Duration
}

type User struct {
	Name string
}
type DB struct {
	cfg Config
}

func (d *DB) SelectUser(ctx context.Context, email string) (User, error) {
	ctx2, cancel := context.WithTimeout(ctx, d.cfg.SelectTimeout)
	defer cancel()

	timer := time.NewTimer(1 * time.Second)
	select {
	case <-timer.C:
		return User{Name: "Gosha"}, nil
	case <-ctx2.Done():
		return User{}, ctx2.Err()
	}
}

type Handler struct {
	db *DB
}

type Request struct {
	Email string
}

type Response struct {
	User User
}

func (h *Handler) HandleAPI(ctx context.Context, req Request) (Response, error) {
	u, err := h.db.SelectUser(ctx, req.Email)
	if err != nil {
		return Response{}, err
	}

	return Response{User: u}, nil
}

func main() {
	cfg := Config{SelectTimeout: timeoutDuration}
	db := DB{cfg: cfg}
	handler := Handler{db: &db}
	ctx, cancel := context.WithCancel(context.Background())

	time.AfterFunc(cancelDuration, cancel)

	req := Request{Email: "test@yandex.ru"}
	resp, err := handler.HandleAPI(ctx, req)
	fmt.Println(resp, err)
}
