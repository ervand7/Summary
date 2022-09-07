package main

import (
	"context"
	"fmt"
	"net/http"
	"time"
)

/*
Важно: методы Query() или Exec() (без Context) под капотом используют
context.Background. Контекст в операциях с БД присутствует всегда.
Если вы пользуетесь инструментарием context.Context,
нужно применять методы QueryContext() и ExecContext(),
позволяющие установить контекст явно.
*/

func MyHandler(w http.ResponseWriter, r *http.Request) {
	// наследуем контекcт запроса r *http.Request,
	// оснащая его Timeout
	ctx, cancel := context.WithTimeout(r.Context(), 5*time.Second)
	// не забываем освободить ресурс
	defer cancel()

	/*
		// делаем обращение к db в рамках полученного контекста
		rows, err := db.QueryContext(ctx, "SELECT something")
		// отрабатываем запрос
		// ...
	*/
	fmt.Println(ctx)

}
