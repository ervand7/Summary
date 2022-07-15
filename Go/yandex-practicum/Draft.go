package main

import "fmt"

type input struct {
	a       int
	b       int
	counter int
}

func f(a, b, counter int) {
	if counter == 0 {
		panic(`counter equals 0`)
	}
	f(b, a/b, counter-1)
}

func test(a, b, counter int) (err error) {
	defer func() {
		if p := recover(); p != nil {
			err = fmt.Errorf("%v", p)
		}
	}()
	f(a, b, counter)
	return nil
}

func main() {
	for _, pars := range []input{
		{10, 5, 3},
		{100, 7, 10},
		{1, 1, 1000},
	} {
		fmt.Printf("(%d, %d, %d) => %v\r\n", pars.a, pars.b, pars.counter,
			test(pars.a, pars.b, pars.counter))
	}
}
