package main

import (
	"fmt"
	"net/http"
	"net/http/cookiejar"
)

func main() {
	client := http.Client{}
	response, err := client.Get("http://127.0.0.1:8000/api/v1/feedbacks_list/")
	fmt.Println(response, err)

	cookie := &http.Cookie{
		Name:   "token",
		Value:  "some_token",
		MaxAge: 300,
	}
	jar, err := cookiejar.New(nil)
	if err != nil {
		fmt.Println(err)
	} else {
		/*
			Client.Jar — это хранилище cookie клиента. Клиент сам извлекает куки
			из ответов сервера и помещает туда. Если вы не пользуетесь клиентом или
			хотите исследовать куки из http.Response, полученные от сервера, можете
			воспользоваться методом Response.Cookies().
		*/
		client.Jar = jar
	}

	fmt.Println(cookie)
	/*
		// куки можно устанавливать клиенту для всех запросов по определённому URL
		client.Jar.SetCookies(url, []*http.Cookie{cookie})
		// а можно добавлять к конкретному запросу
		request.AddCookie(cookie)
	*/
}
