package main

// we can not get size of type:

func main() {
	type a struct {
		field1 int
	}
	// fmt.Println(unsafe.Sizeof(a)) - будет ошибка
}
