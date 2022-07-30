package main

import (
	"fmt"
	"net/http"
)

/*
Теперь напишем обработчик, который разбирает запрос и конструирует ответ
на основе полученных данных, — упрощённый пример авторизации реквизитами
login–password. Принимать реквизиты будем в HTML <form> на URL mydomain.com/login.
Минимальная форма может выглядеть так:
*/

var form = `<html>
    <head>
    <title></title>
    </head>
    <body>
        <form action="/login" method="post">
            <label>Логин</label><input type="text" name="login">
            <label>Пароль<input type="password" name="password">
            <input type="submit" value="Login">
        </form>
    </body>
</html>`

/*
Методом GET обработчик запросов будет предоставлять форму для заполнения.
По запросу методом POST будет обрабатывать полученные реквизиты.
*/

func Login(w http.ResponseWriter, r *http.Request) {
	// проверяем, каким методом получили запрос
	switch r.Method {
	// если методом POST
	case "POST":
		// проверяем форму
		if err := r.ParseForm(); err != nil {
			// если не заполнена, возвращаем код ошибки
			http.Error(w, "Bad auth", 401)
			return
		}
		login := r.FormValue("login")
		password := r.FormValue("password")
		// проверяем пароль вспомогательной функцией
		if !Auth(login, password) {
			w.Header().Set("Content-Type", "text/plain; charset=utf-8")
			// если пароль не верен, указываем код ошибки в заголовке
			w.WriteHeader(401)
			// пишем в тело ответа
			fmt.Fprintln(w, "Wrong password")
			return
		}
		/*
			при успешной авторизации обрабатываем запрос:
			например, передаём другому обработчику
			AuthorisedHandler(w, r)
			в остальных случаях предлагаем форму авторизации
		*/

	default:
		fmt.Fprint(w, form)
	}
}

var Logins = make(map[string]string)

// Auth — вспомогательная функция авторизации
// за пределами урока реализация может выглядеть так
func Auth(l, p string) bool {
	pass, ok := Logins[l]
	return ok && p == pass
}
