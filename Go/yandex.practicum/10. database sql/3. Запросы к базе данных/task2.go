package main

import (
	"context"
	"database/sql"
	"fmt"
	_ "github.com/jackc/pgx/v4/stdlib"
)

type video struct {
	channelTitle string
	sum          int64
	count        int64
	avg          float64
}

const Limit = 30

func Videos(ctx context.Context, db *sql.DB, limit int) ([]video, error) {
	videos := make([]video, 0, limit)

	rows, err := db.QueryContext(ctx, "select \"channel_title\", sum(\"views\"), count(\"video_id\"), avg(\"views\")\nfrom videos\ngroup by channel_title\norder by sum(\"views\") desc\nlimit $1", limit)
	if err != nil {
		return nil, err
	}

	// обязательно закрываем перед возвратом функции
	defer rows.Close()

	// пробегаем по всем записям
	for rows.Next() {
		var v video
		err = rows.Scan(&v.channelTitle, &v.sum, &v.count, &v.avg)
		if err != nil {
			return nil, err
		}

		videos = append(videos, v)
	}

	// проверяем на ошибки
	err = rows.Err()
	if err != nil {
		return nil, err
	}
	return videos, nil
}

func main() {
	db, err := sql.Open("pgx",
		"user=ervand password=ervand dbname=go_lesson10 host=localhost port=5432 sslmode=disable")
	if err != nil {
		panic(err)
	}
	defer db.Close()
	result, _ := Videos(context.Background(), db, Limit)
	fmt.Println(result)
}
