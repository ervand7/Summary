package main

import (
	"context"
	"database/sql"
	"encoding/csv"
	"errors"
	_ "github.com/jackc/pgx/v4/stdlib"
	"io"
	"log"
	"os"
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

type VideoDB struct {
	*sql.DB
	buffer []Video
}

func NewVideoDB(db *sql.DB) (*VideoDB, error) {
	return &VideoDB{
		DB:     db,
		buffer: make([]Video, 0, 1000),
	}, nil
}

func main() {
	db, err := sql.Open("pgx",
		"user=ervand password=ervand dbname=go_lesson10 host=localhost port=5432 sslmode=disable")
	if err != nil {
		log.Fatal(err.Error())
	}
	defer db.Close()

	videoDB, err := NewVideoDB(db)
	if err != nil {
		log.Fatal(err.Error())
	}

	// открываем csv-файл
	file, err := os.Open("/Users/ervand_agadzhanyan/Desktop/Summary/Go/yandex.practicum/10. database sql/4. Запросы вставки данных, обновления и удаления/USvideos.csv")
	if err != nil {
		log.Fatal(err)
	}

	// конструируем Reader из пакета encoding/csv. Он умеет читать строки csv-файла
	csvReader := csv.NewReader(file)
	VideoFromCsvToDB(csvReader, videoDB)
}

func (db *VideoDB) AddVideo(v Video) error {
	db.buffer = append(db.buffer, v)

	if cap(db.buffer) == len(db.buffer) {
		err := db.Flush()
		if err != nil {
			return errors.New("cannot add records to the database")
		}
	}
	return nil
}

func (db *VideoDB) Flush() error {
	// шаг 1 — объявляем транзакцию
	tx, err := db.Begin()
	if err != nil {
		return err
	}
	// шаг 1.1 — если возникает ошибка, откатываем изменения
	defer tx.Rollback()

	// шаг 2 — готовим инструкцию
	ctx := context.Background()
	stmt, err := tx.PrepareContext(ctx, "INSERT INTO videos(title, description, views, likes) VALUES($1,$2,$3,$4)")
	if err != nil {
		return err
	}
	// шаг 2.1 — не забываем закрыть инструкцию, когда она больше не нужна
	defer stmt.Close()

	for _, v := range db.buffer {
		// шаг 3 — указываем, что каждое видео будет добавлено в транзакцию
		if _, err = stmt.ExecContext(ctx, v.Title, v.Description, v.Views, v.Likes); err != nil {
			return err
		}
	}

	// шаг 4 — сохраняем изменения
	if err := tx.Commit(); err != nil {
		log.Fatalf("update drivers: unable to commit: %v", err)
		return err
	}

	// шаг 5 - очищаем буффер
	db.buffer = db.buffer[:0]
	return nil
}

func VideoFromCsvToDB(r *csv.Reader, db *VideoDB) error {
	// проверим на всякий случай
	if db.DB == nil {
		return errors.New("you haven`t opened the database connection")
	}
	// готовим контейнер для проверок
	check := new(string)
	// готовим стейтмент
	stmt, err := db.Prepare(`SELECT "title" FROM videos WHERE "title" = $1`)
	if err != nil {
		return err
	}

	for {
		l, err := r.Read()
		if errors.Is(err, io.EOF) {
			break
		} else if err != nil {
			log.Panic(err)
		}

		// проверяем, есть ли видео в базе
		row := stmt.QueryRow(l[2])
		// хотим убедиться, нашлось или нет
		if err := row.Scan(check); err != sql.ErrNoRows {
			continue
		}

		v := Video{
			Id:           l[0],
			TrendingDate: l[1],
			Title:        l[2],
			Channel:      l[3],
			CategoryId:   l[4],
			// и так далее
		}

		err = db.AddVideo(v)
		if err != nil {
			return err
		}

	}
	// в конце записываем оставшиеся данные из буфера
	db.Flush()
	return nil
}
