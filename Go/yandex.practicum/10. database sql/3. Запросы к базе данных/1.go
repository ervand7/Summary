package main

import (
	"context"
	"database/sql"
	"fmt"
	_ "github.com/mattn/go-sqlite3"
	"log"
	"time"
)

func main() {
	db, err := sql.Open("sqlite3",
		"identifier.sqlite")
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
