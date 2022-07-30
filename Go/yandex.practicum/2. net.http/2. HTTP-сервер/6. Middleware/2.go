package main

import "net/http"

/*
Множественное вложение функций выглядит не очень красиво.
В декоративных целях можно написать небольшой хелпер.
*/

type Middleware func(http.Handler) http.Handler

func Conveyor(h http.Handler, middlewares ...Middleware) http.Handler {
	for _, middleware := range middlewares {
		h = middleware(h)
	}
	return h
}

func main() {
	/*
	   Тогда будет симпатичнее:
	   http.Handle("/", Conveyor(finalHandler, middleware1, middleware2, middleware3))
	*/
}
