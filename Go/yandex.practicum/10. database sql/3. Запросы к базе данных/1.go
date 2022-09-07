package main

import (
	"context"
	"database/sql"
	"fmt"
	_ "github.com/jackc/pgx/v4/stdlib"
	"log"
	"time"
)

func main() {
	db, err := sql.Open("pgx",
		"user=ervand password=ervand dbname=go_lesson10 host=localhost port=5432 sslmode=disable")
	if err != nil {
		panic(err)
	}
	defer db.Close()
	// готовим контейнер
	var id int64

	// конструируем контекст с 5-секундным тайм-аутом
	// после 5 секунд затянувшаяся операция с БД будет прервана
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	// не забываем освободить ресурс
	defer cancel()

	// обращаемся к БД
	row := db.QueryRowContext(ctx, "SELECT COUNT(*) as count FROM videos")
	// разбираем результат
	err = row.Scan(&id)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(id)
}
