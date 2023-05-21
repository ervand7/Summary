package main

/*
Сначала импортируем пакет pprof в приложение, чтобы он зарегистрировал
стандартные обработчики.
Инструмент pprof регистрирует обработчики при инициализации пакета в функции init.

Работать с pprof и просматривать результаты профилирования можно в веб-интерфейсе.
Но pprof не запускает HTTP-сервер самостоятельно, он только регистрирует
обработчик на адрес /debug/pprof/. Поэтому если приложение не использует
HTTP-сервер для собственных нужд, то его нужно добавить и запустить
специально для pprof. Это делается в последней строке кода:
*/

import (
	"net/http"
	_ "net/http/pprof" // подключаем пакет pprof
)

const (
	addr    = ":8080"    // адрес сервера
	maxSize = 10_000_000 // будем растить слайс до 10 миллионов элементов
)

func foo() {
	// полезная нагрузка
	for {
		var s []int
		for i := 0; i < maxSize; i++ {
			s = append(s, i)
		}
	}
}

func main() {
	/*
		Важно! В Urlshortener в main.go пришлось добавлять:
		go func() {
			log.Println(http.ListenAndServe(":6060", nil))
		}()

		И запускать так:
		go tool pprof -http=":9090" -seconds=30 -edgefraction 0 -nodefraction 0 -nodecount 100000 http://localhost:6060/debug/pprof/heap

	*/

	go foo()                       // запускаем полезную нагрузку в фоне
	http.ListenAndServe(addr, nil) // запускаем сервер
}
