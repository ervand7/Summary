package main

import (
	"database/sql"
	"fmt"
	_ "github.com/jackc/pgx/v4/stdlib"
	"log"
	"time"
)

type (
	Video struct {
		Id,
		Title,
		Channel,
		Description,
		CategoryId string

		TrendingDate string
		PublishTime  time.Time

		Tags []Tag

		Views    int
		Likes    int
		Dislikes int
		Comments int

		CommentsDisabled    bool
		RatingDisabled      bool
		VideoErrorOrRemoved bool

		ThumbnailLink string
	}

	Tag struct {
		Name string
	}
)

func main() {
	db, err := sql.Open("pgx",
		"user=ervand password=ervand dbname=go_lesson10 host=localhost port=5432 sslmode=disable")
	if err != nil {
		log.Fatal(err.Error())
	}
	defer db.Close()

	upStmt, err := db.Prepare("UPDATE videos SET description = $1, views = $2, likes = $3 WHERE title = $4")
	if err != nil {
		panic(err)
	}
	v := Video{Description: "qwe", Views: 123, Likes: 123, Title: "[OFFICIAL VIDEO] Deck The Halls - Pentatonix"}
	count, err := Update(upStmt, v)
	if err != nil {
		log.Fatal(err.Error())
	}
	fmt.Printf("Кол-во обновленых записей: %d", count)

}

func Update(upStmt *sql.Stmt, v Video) (exists int64, err error) {
	// используем подготовленный стейтмент
	res, err := upStmt.Exec(v.Description, v.Views, v.Likes, v.Title)
	if err != nil {
		return
	}
	// посмотрим, сколько записей было обновлено
	exists, err = res.RowsAffected()
	return
}
