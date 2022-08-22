package main

import (
	"flag"
	"fmt"
)

/*
Функция flag.Parse() обрабатывает флаги. Однако не у всех аргументов командной
строки обязательно должен быть синтаксис и семантика флагов.
Например, утилите можно передавать имя файла для чтения.

У имени нет семантики флага — это просто аргумент. Когда функция flag.Parse()
встречает аргумент, не соответствующий стандарту парсинга,
такой аргумент и все последующие становятся для неё позиционными.
Они рассматриваются как слайс строк, и их можно вызвать функциями flag.Arg() и flag.Args():
 - flag.Arg(i int) string возвращает i-й аргумент в виде строки,
 - flag.Args() []string возвращает все позиционные аргументы в виде слайса строк.
Утилита, работающая с файлами edit -enc=UTF8 file/name, может содержать такой код:
*/

func main() {
	var enc string
	flag.StringVar(&enc, "enc", "UTF8", "Text encoding. Possible values: UTF8 UTF16 ascii")
	flag.Parse()
	fmt.Println(flag.Arg(1))
	fmt.Println(flag.Args())
}

/*
$ go run 6.\ Позиционные\ аргументы.go --enc=UTF16 xf cg sdf cgh drt
xf
[xf cg sdf cgh drt]
*/
