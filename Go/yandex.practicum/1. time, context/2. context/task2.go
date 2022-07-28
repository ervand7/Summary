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
	waitDur    = 1 * time.Second
	cancelDur  = 2000 * time.Millisecond
	timeoutDur = 500 * time.Millisecond
)

type Config struct {
	SelectTimeout time.Duration
}

type DB_ struct {
	cfg Config
}

type User_ struct {
	Name string
}

func (d *DB_) SelectUser(ctx context.Context, email string) (User_, error) {
	ctx2, cancel := context.WithTimeout(ctx, d.cfg.SelectTimeout)
	defer cancel()

	timer := time.NewTimer(1 * time.Second)
	select {
	case <-timer.C:
		return User_{Name: "Gosha"}, nil
	case <-ctx2.Done():
		return User_{}, ctx2.Err()
	}
}

type Handler_ struct {
	db *DB_
}

type Request_ struct {
	Email string
}

type Response_ struct {
	User_ User_
}

func (h *Handler_) HandleAPI(ctx context.Context, req Request_) (Response_, error) {
	u, err := h.db.SelectUser(ctx, req.Email)
	if err != nil {
		return Response_{}, err
	}

	return Response_{User_: u}, nil
}

func main() {
	cfg := Config{SelectTimeout: timeoutDur}
	db := DB_{cfg: cfg}
	handler := Handler_{db: &db}
	ctx, cancel := context.WithCancel(context.Background())

	time.AfterFunc(cancelDur, cancel)

	req := Request_{Email: "test@yandex.ru"}
	resp, err := handler.HandleAPI(ctx, req)
	fmt.Println(resp, err)
}
