package main

func main() {
	/*
		Для указателей на структуры в Go есть возможность неявного
		разыменования при доступе к полям структуры
	*/
	type A struct {
		IntField int
	}

	p := &A{}
	p.IntField = 42 // вместо (*p).IntField = 42
}
