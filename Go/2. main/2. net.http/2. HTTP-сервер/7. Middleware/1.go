package main

import "net/http"

/*
Среди бэкенд-разработчиков популярна концепция middleware — конвейерной
обработки запроса несколькими хендлерами. В разработке часто используют
сторонние маршрутизаторы, которые предоставляют удобный интерфейс для создания
и подключения middleware. О сторонних библиотеках подробно расскажем в
следующих уроках темы. А сейчас покажем, как сделать конвейерную обработку
запросов средствами stdlib, — так будет понятнее, что происходит под капотом.

Соберём конвейер. Для этого понадобится такая сигнатура:
*/

// middleware принимает параметром Handler и возвращает тоже Handler.
func middleware(next http.Handler) http.Handler {
	// собираем Handler приведением типа
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// здесь пишем логику обработки
		// например, разрешаем запросы cross-domain
		// w.Header().Set("Access-Control-Allow-Origin", "*")
		// ...
		// замыкание — используем ServeHTTP следующего хендлера
		next.ServeHTTP(w, r)
	})
}

func main() {
	/*
		Тогда с finalHandler можем написать:
		http.Handle("/", middleware(finalHandler))
	*/
}
