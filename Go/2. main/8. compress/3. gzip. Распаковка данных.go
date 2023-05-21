package main

import (
	"compress/gzip"
	"fmt"
	"io"
	"net/http"
)

/*
Если вы отправляете запрос HTTP-серверу стандартным Go-клиентом,
он автоматически добавляет заголовок Accept-Encoding: gzip и
распаковывает полученный ответ. В этом случае не нужно добавлять
распаковку в код клиента.

Рассмотрим ситуацию, когда серверу может прийти запрос со сжатыми данными.
Приведённый ниже обработчик получает в теле запроса сжатые данные в формате
gzip, распаковывает и возвращает их оригинальный размер.
*/

// LengthHandle возвращает размер распакованных данных.
func LengthHandle(w http.ResponseWriter, r *http.Request) {
	// создаём *gzip.Reader, который будет читать тело запроса и распаковывать его
	gz, err := gzip.NewReader(r.Body)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	// не забывайте потом закрыть *gzip.Reader
	defer gz.Close()

	// при чтении вернётся распакованный слайс байт
	body, err := io.ReadAll(gz)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	fmt.Fprintf(w, "Length: %d", len(body))
}

/*
Распаковка сжатых gzip-данных не сильно отличается от распаковки Deflate.
Этот обработчик считает, что к нему приходят только упакованные данные.
Если в запросе отправить обычный текст, вернётся ошибка.
*/
