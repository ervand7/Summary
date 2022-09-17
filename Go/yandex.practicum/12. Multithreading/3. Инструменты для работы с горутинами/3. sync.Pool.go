package main

import (
	"bytes"
	"fmt"
	"io"
	"os"
	"sync"
	"time"
)

/*
Если программа постоянно создаёт одни и те же объекты, её работу поможет
оптимизировать sync.Pool. Он создаёт пул однотипных объектов, которые можно
использовать повторно. Это позволяет экономить время на сборщике мусора и
инициализации новых объектов. С переменной sync.Pool можно безопасно работать
в разных горутинах.
*/

var bufPool = sync.Pool{
	// функция создаёт новые объекты, если в пуле нечего переиспользовать
	New: func() interface{} {
		return new(bytes.Buffer)
	},
}

func Log(w io.Writer, key, val string) {
	b := bufPool.Get().(*bytes.Buffer) // забираем из пула объект
	b.Reset()

	fmt.Fprintf(b, "%s %s=%s", time.Now().UTC().Format(time.RFC3339), key, val)
	w.Write(b.Bytes())

	bufPool.Put(b) // возвращаем в пул
}

func main() {
	Log(os.Stdout, "path", "/search?q=flowers")
}
