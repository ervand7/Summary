package main

import (
	"fmt"
	"net/http"
)

// Рассмотрим пример middleware, которая перед каждой функцией выводит сообщение
// "Hi! I'm middleware". А после выполнения функции — "Bye!".

// HiByeMiddleware выводит сообщение перед и после основной функции.
func HiByeMiddleware(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("Hi! I'm middleware")
		next(w, r)
		fmt.Println("Bye!")
	}
}
