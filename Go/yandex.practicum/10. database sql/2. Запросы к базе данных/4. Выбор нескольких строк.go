package main

import (
	"context"
	"database/sql"
	"fmt"
	_ "github.com/mattn/go-sqlite3"
)

/*
Параметр ? будет разным для разных типов баз данных.
Для MySQL, SQLite3 и MS SQL это будет ?. Для PostgreSQL — $N, число. Для Oracle — :param.
*/

// Video — структура видео.
type Video struct {
	Id    string
	Title string
	Views int64
}

// limit — максимальное количество записей.
const limit = 20

func QueryVideos(ctx context.Context, db *sql.DB, limit int) ([]Video, error) {
	videos := make([]Video, 0, limit)

	rows, err := db.QueryContext(ctx, "SELECT video_id, title, views from videos ORDER BY views LIMIT ?", limit)
	if err != nil {
		return nil, err
	}

	// обязательно закрываем перед возвратом функции
	defer rows.Close()

	// пробегаем по всем записям
	for rows.Next() {
		var v Video
		err = rows.Scan(&v.Id, &v.Title, &v.Views)
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
	db, err := sql.Open("sqlite3",
		"identifier.sqlite")
	if err != nil {
		panic(err)
	}
	defer db.Close()
	result, _ := QueryVideos(context.Background(), db, limit)
	fmt.Println(result)
}
