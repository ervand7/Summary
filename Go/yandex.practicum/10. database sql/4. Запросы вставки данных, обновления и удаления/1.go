package main

import (
	"context"
	"database/sql"
	"encoding/csv"
	"fmt"
	_ "github.com/jackc/pgx/v4/stdlib"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
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
	// инициируем контекст
	ctx := context.Background()
	// открываем соединение с БД
	db, err := sql.Open("pgx",
		"user=ervand password=ervand dbname=go_lesson10 host=localhost port=5432 sslmode=disable")
	if err != nil {
		log.Fatal(err.Error())
	}
	defer db.Close()

	// открываем csv-файл
	file, err := os.Open("/Users/ervand_agadzhanyan/Desktop/Summary/Go/yandex.practicum/10. database sql/4. Запросы вставки данных, обновления и удаления/USvideos.csv")
	if err != nil {
		log.Fatal(err)
	}

	// конструируем Reader из пакета encoding/csv. Он умеет читать строки csv-файла
	csvReader := csv.NewReader(file)
	// читаем записи из файла в слайс []Video вспомогательной функцией
	start := time.Now()
	videos, err := readVideos(csvReader)
	if err != nil {
		log.Fatal(err)
	}

	// записываем []Video в базу данных в инициированном контексте
	// тоже вспомогательной функцией
	err = insertVideos(ctx, db, videos)
	if err != nil {
		log.Fatal(err)
	}
	end := time.Since(start).Milliseconds()
	fmt.Printf("Всего csv-записей %v\n", len(videos))
	fmt.Printf("Время исполнения запросов: %d", end)
}

func readVideos(r *csv.Reader) ([]Video, error) {
	var videos []Video
	for {
		// csv.Reader за одну операцию Read() считывает одну csv-запись
		l, err := r.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			return nil, err
		}
		// инициализируем целевую структуру, в которую будем делать разбор csv-записи
		// сюда сразу можно добавить все строковые записи
		v := Video{
			Id:            l[0],
			TrendingDate:  l[1],
			Title:         l[2],
			Channel:       l[3],
			CategoryId:    l[4],
			ThumbnailLink: l[11],
			Description:   l[15],
		}
		// далее делаем парсинг строковых записей в типизированные поля структуры
		if v.PublishTime, err = time.Parse(time.RFC3339, l[5]); err != nil {
			continue
		}
		tgs := strings.Split(l[6], " ")
		for _, tg := range tgs {
			v.Tags = append(v.Tags, Tag{tg})
		}
		if v.Views, err = strconv.Atoi(l[7]); err != nil {
			continue
		}
		if v.Likes, err = strconv.Atoi(l[8]); err != nil {
			continue
		}
		if v.Dislikes, err = strconv.Atoi(l[9]); err != nil {
			continue
		}
		if v.Comments, err = strconv.Atoi(l[10]); err != nil {
			continue
		}
		if v.CommentsDisabled, err = strconv.ParseBool(l[12]); err != nil {
			continue
		}
		if v.RatingDisabled, err = strconv.ParseBool(l[13]); err != nil {
			continue
		}
		if v.VideoErrorOrRemoved, err = strconv.ParseBool(l[14]); err != nil {
			continue
		}

		// добавляем полученную структуру в слайс
		videos = append(videos, v)
	}
	return videos, nil
}

func insertVideos(ctx context.Context, db *sql.DB, videos []Video) error {
	for _, v := range videos {
		_, err := db.ExecContext(ctx, `INSERT INTO videos(
                   title, description, views, likes
                   ) VALUES($1,$2,$3,$4)`, v.Title, v.Description, v.Views, v.Likes)
		if err != nil {
			return err
		}
	}
	return nil
}
