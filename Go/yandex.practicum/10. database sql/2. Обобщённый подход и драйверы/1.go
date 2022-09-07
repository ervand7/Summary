package main

/*
Обратите внимание: пакет go-sqlite3 импортирован анонимно.
Не получится обращаться напрямую к go-sqlite3.
Внутри пакет зарегистрирует себя самостоятельно и
будет доступен для использования через sql.DB.

Если нас не интересует пространство имён драйвера
github.com/mattn/go-sqlite3, зачем вообще его импортировать?
Что происходит при этом импорте?
Правильный ответ:
Отрабатывают init()-функции пакета драйвера.
Да. Инициализация database/sql драйвером делается именно
в init()-функциях драйвера, которые вызываются при импорте
*/

import (
	"database/sql"
	_ "github.com/mattn/go-sqlite3"
)

func main() {
	db, err := sql.Open("sqlite3",
		"db.db")
	if err != nil {
		panic(err)
	}
	defer db.Close()
	// работаем с базой
	// ...

	/*
		можем продиагностировать соединение
		ctx, cancel := context.WithTimeout(ctx, 1*time.Second)
		defer cancel()
		if err = db.PingContext(ctx); err != nil {
			panic(err)
		}
	*/
}
