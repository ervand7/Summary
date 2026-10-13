package main

import (
	"fmt"
	"unsafe"
)

// unsafe.Sizeof для любой строки будет выдавать 16 байт
// https://stackoverflow.com/questions/65878177/unsafe-sizeof-says-any-string-takes-16-bytes-but-how

func main() {
	var a string
	fmt.Println(unsafe.Sizeof(a)) // 16

	a = "Hello world"
	fmt.Println(unsafe.Sizeof(a)) // 16
}

/*
Почему?
Потому что строка в Go представлена структурой, которая содержит два поля:

1. **Указатель на данные** (`data`): это указатель на первый байт данных строки.
2. **Длина строки** (`len`): это целое число, представляющее длину строки в байтах.

Эта структура в Go выглядит следующим образом:

```go
type string struct {
    data uintptr
    len  int
}
```

- **8 байт** для указателя на данные.
- **8 байт** для длины строки.

Итого: **8 байт + 8 байт = 16 байт**.
*/
