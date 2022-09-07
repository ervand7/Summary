package main

import (
	"database/sql"
	"fmt"
	_ "github.com/mattn/go-sqlite3"
	"time"
)

/*
В базе есть атрибут trending_date. Его значения могут быть такими:
	18.31.05,
	17.29.12,
	05.01.12.
Формат поля: год.день.месяц.
Преобразуйте дату в формат time.Time. Выведите количество роликов по каждому дню trending_date с помощью Go.
*/

type Trend struct {
	T     time.Time
	Count int
}

func TrendingCount() ([]Trend, error) {
	db, err := sql.Open("sqlite3",
		"identifier.sqlite")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	rows, err := db.Query("SELECT trending_date, COUNT(trending_date) FROM videos GROUP BY trending_date")
	if err != nil {
		return nil, err
	}

	trends := make([]Trend, 0)
	date := new(string)
	for rows.Next() {
		trend := Trend{}
		err = rows.Scan(date, &trend.Count)
		if err != nil {
			return nil, err
		}
		if trend.T, err = time.Parse("06.02.01", *date); err != nil {
			return nil, err
		}
		trends = append(trends, trend)
	}
	return trends, nil
}

func main() {
	result, _ := TrendingCount()
	fmt.Println(result)
}
