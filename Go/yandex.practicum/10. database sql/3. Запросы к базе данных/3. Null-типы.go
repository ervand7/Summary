package main

import (
	"database/sql"
	"fmt"
	_ "github.com/mattn/go-sqlite3"
)

func main() {
	db, err := sql.Open("sqlite3",
		"identifier.sqlite")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	var s sql.NullString

	SomeID := "2kyS6SvSYSE"
	err = db.QueryRow("SELECT title FROM videos WHERE video_id = ?", SomeID).Scan(&s)
	// в запросе использован контейнер "?",
	// которому будет передано значение SomeID
	// так можно строить запрос с параметрами
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
