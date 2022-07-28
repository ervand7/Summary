package main

/*
для bool значение по умолчанию — false;
для числовых типов — 0;
для ссылочных типов — nil или пустой указатель;
для string — пустая строка длиной 0.
*/

func main() {
	var str string
	// можно использовать одно из этих условий для проверки пустой строки
	if str == "" || len(str) == 0 {
		println("The string in empty")
	}
}
