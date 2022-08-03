package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

/*
Прописываем логику авторизации с помощью стандартной библиотеки.
*/

var bearer = "Bearer <Token>"

func main() {
	// создаём новый запрос
	req, err := http.NewRequest("GET", "https://yandex.ru", nil)

	// добавляем авторизацию
	req.Header.Add("Authorization", bearer)

	// создаём клиента
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		log.Println("Error on response.\n[ERROR] -", err)
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	// продолжаем работу
	fmt.Println(string(body))
}
