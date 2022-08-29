package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	// декларируем наборы флагов для subcommand
	getFlags := flag.NewFlagSet("get", flag.ExitOnError)
	setFlags := flag.NewFlagSet("set", flag.ExitOnError)
	// декларируем флаги для набора getFlags
	getKey := getFlags.String("key", "", "Key string")
	// флаги набора setFlags
	setKey := setFlags.String("key", "", "Key string")
	setValue := setFlags.String("value", "", "Value string")

	osArgs := os.Args
	fmt.Println(osArgs)
	// проверяем, задана ли подкоманда
	// os.Arg[0] имя команды
	// os.Arg[1] имя подкоманды
	if len(os.Args) < 2 {
		fmt.Println("set or get subcommand required")
		os.Exit(1)
	}

	// в зависимости от переданной подкоманды
	// делаем парсинг флагов соответствующего набора
	// передаём функции FlagSet.Parse() аргументы командной строки
	// os.Args[2:] содержит все аргументы,
	// следующие за os.Args[1] — именем подкоманды
	switch os.Args[1] {
	case "get":
		getFlags.Parse(os.Args[2:])
	case "set":
		setFlags.Parse(os.Args[2:])
	default:
		flag.PrintDefaults()
		os.Exit(1)
	}
	// проверяем, какой набор флагов использовался,
	// то есть какая подкоманда была передана, вызовом FlagSet.Parsed()
	// FlagSet.Parsed() возвращает false, если
	// парсинг флагов набора не проводился
	if getFlags.Parsed() {
		// логика для get
	}
	if setFlags.Parsed() {
		// логика для set
	}

	fmt.Println(getKey, setKey, setValue) // for debug
}

/*
$ go run 7.\ flag.FlagSet\ —\ наборы\ флагов.go get -key key111
или
$ go run 7.\ flag.FlagSet\ —\ наборы\ флагов.go set -key key222 -value value222
*/
