package main

import (
	"context"
	"database/sql"
	_ "github.com/jackc/pgx/v4/stdlib"
	"time"
)

/*
Обратите внимание: пакет github.com/jackc/pgx/v4/stdlib импортирован анонимно.
Не получится обращаться напрямую к pgx.
Внутри пакет зарегистрирует себя самостоятельно и
будет доступен для использования через sql.DB.

Если нас не интересует пространство имён драйвера
github.com/jackc/pgx/v4/stdlib, зачем вообще его импортировать?
Что происходит при этом импорте?
Правильный ответ:
Отрабатывают init()-функции пакета драйвера.
Да. Инициализация database/sql драйвером делается именно
в init()-функциях драйвера, которые вызываются при импорте
*/

func main() {
	db, err := sql.Open("pgx",
		"user=ervand password=ervand dbname=go_lesson10 host=localhost port=5432 sslmode=disable")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	// можем продиагностировать соединение
	ctx := context.Background()
	ctx, cancel := context.WithTimeout(ctx, 1*time.Second)
	defer cancel()
	if err = db.PingContext(ctx); err != nil {
		panic(err)
	}
}
