package main

import (
	"fmt"
	"sync"
)

/*
Если программа постоянно создаёт одни и те же объекты, её работу поможет
оптимизировать sync.Pool. Он создаёт пул однотипных объектов, которые можно
использовать повторно. Это позволяет экономить время на сборщике мусора и
инициализации новых объектов. С переменной sync.Pool можно безопасно работать
в разных горутинах.

Важно! В яндекс.практикуме плохо это описано. Вот хорошие статьи:
https://habr.com/ru/articles/277137/
https://dev-gang.ru/article/go-ponjat-dizain-syncpool-cpvecztx8e/
*/

const maxCap = 1024

var bytesPool = sync.Pool{
	// функция New сработает только если пулл пуст
	New: func() interface{} { return []byte{} },
}

// положить
func putBytes(b []byte) {
	if cap(b) <= maxCap {
		b = b[:0] // сброс
		bytesPool.Put(b)
	}
}

// получить
func getBytes() (b []byte) {
	ifc := bytesPool.Get()
	if ifc != nil {
		b = ifc.([]byte)
	}
	return b
}

func main() {
	slice := make([]byte, 10, 10)
	putBytes(slice)
	result := getBytes()
	fmt.Println(result)
}
