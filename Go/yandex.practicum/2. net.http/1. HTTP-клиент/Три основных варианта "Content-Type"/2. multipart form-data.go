//https://ru.wikipedia.org/wiki/Multipart/form-data
package main

import (
	"bytes"
	"fmt"
	"io"
	"mime/multipart"
	"net/http"
	"os"
)

func main() {
	// открываем файл
	filename := "form.txt"
	file, _ := os.Open(filename)
	// не забываем закрыть
	defer file.Close()
	// конструируем буфер
	body := &bytes.Buffer{}
	// на основе буфера конструируем multipart.Writer из пакета mime/multipart
	writer := multipart.NewWriter(body)
	// готовим форму для отправки файла на сервер
	part, err := writer.CreateFormFile("uploadfile", filename)
	if err != nil {
		// обработаем ошибку
	}
	// копируем файл в форму
	// multipart.Writer отформатирует данные и запишет в предоставленный буфер
	_, err = io.Copy(part, file)
	if err != nil {
		// обработаем ошибку
	}
	writer.Close()
	// конструируем запрос
	request, err := http.NewRequest(
		"POST",
		"http://127.0.0.1:8000/api/v1/feedbacks_list/",
		body,
	)
	if err != nil {
		// обработаем ошибку
	}
	// добавляем заголовок запроса
	request.Header.Add("Content-Type", writer.FormDataContentType())

	fmt.Println(request.Body)
}
