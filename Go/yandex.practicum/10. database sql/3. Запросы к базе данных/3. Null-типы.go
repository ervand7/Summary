package main

import (
	"database/sql"
	"fmt"
	_ "github.com/jackc/pgx/v4/stdlib"
)

func main() {
	db, err := sql.Open("pgx",
		"user=ervand password=ervand dbname=go_lesson10 host=localhost port=5432 sslmode=disable")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	var s sql.NullString

	SomeID := "2kyS6SvSYSE"
	err = db.QueryRow("SELECT title FROM videos WHERE video_id = $1", SomeID).Scan(&s)
	if err != nil {
		panic(err)
	}
	if s.Valid {
		// если значение было установлено и не было NULL, используем его
		fmt.Println(s.String)
	} else {
		// или понимаем, что значения не было, а был NULL
		fmt.Println("Title not set")
	}
}
