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
	var title, channel_title string
	var views int64

	// конструируем контекст с 5-секундным тайм-аутом
	// после 5 секунд затянувшаяся операция с БД будет прервана
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	// не забываем освободить ресурс
	defer cancel()

	// обращаемся к БД
	row := db.QueryRowContext(ctx, "select title, views, channel_title from videos order by views desc limit 1")
	// разбираем результат
	err = row.Scan(&title, &views, &channel_title)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(title, "\n", views, "\n", channel_title)

}
