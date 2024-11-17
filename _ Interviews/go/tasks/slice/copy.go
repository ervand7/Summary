package main

import "fmt"

type A struct {
	a [][]string
	b []string
}

func main() {
	a1 := A{
		a: [][]string{
			[]string{"11", "12"},
			[]string{"21", "22"},
		},
		b: []string{"1", "2"},
	}

	// iteration 1
	// тут идет один и тот же базовый массив для внешнего и то же самое со внутренними
	a2 := a1
	a1.a[0][0] = "changed"
	a1.b[0] = "changed"
	fmt.Printf("1: %t \n", a1.a[0][0] == a2.a[0][0]) // true
	fmt.Printf("2: %t \n", a1.b[0] == a2.b[0])       // true

	// iteration 2
	// тут просто копируются данные в одни и те же базовые массивы
	copy(a2.a, a1.a)
	copy(a2.b, a1.b)
	fmt.Printf("%p\n", a2.a) // 0x140000780c0
	fmt.Printf("%p\n", a1.a) // 0x140000780c0
	fmt.Printf("%p\n", a2.b) // 0x14000106040
	fmt.Printf("%p\n", a1.b) // 0x14000106040
	a1.a[0][0] = "changed2"
	a1.b[0] = "changed2"
	fmt.Printf("3: %t \n", a1.a[0][0] == a2.a[0][0]) // true
	fmt.Printf("4: %t \n", a1.b[0] == a2.b[0])       // true

	// iteration 3
	// тут сначала создаются значения для a2 с новыми базовыми массивами, но при копировании
	// двумерного массива каждый вложенный слайс копируется с его базовым массивом
	a2.a = make([][]string, len(a2.a))
	a2.b = make([]string, len(a2.b))
	fmt.Printf("%p\n", a2.a) // 0x140000780f0
	fmt.Printf("%p\n", a1.a) // 0x140000780c0
	fmt.Printf("%p\n", a2.b) // 0x14000106060
	fmt.Printf("%p\n", a1.b) // 0x14000106040
	copy(a2.a, a1.a)
	fmt.Printf("%p\n", a2.a[0]) // 0x14000104000
	fmt.Printf("%p\n", a1.a[0]) // 0x14000104000
	copy(a2.b, a1.b)
	a1.a[0][0] = "changed3" // true
	a1.b[0] = "changed3"    // false
	fmt.Printf("5: %t \n", a1.a[0][0] == a2.a[0][0])
	fmt.Printf("6: %t \n", a1.b[0] == a2.b[0])
}
