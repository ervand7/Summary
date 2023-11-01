package main

const size = 4096

func main() {
	s := "HELLO"
	stackCopy(&s, 0, &[size]int{})
}

func stackCopy(s *string, c int, a *[size]int) {
	println(c, s, *s)
	c++
	if c == 10 {
		return
	}

	stackCopy(s, c, a)
}

/*
0 0x1400011ff58 HELLO
1 0x1400011ff58 HELLO
2 0x1400015ff58 HELLO <- CHANGED
3 0x1400015ff58 HELLO
4 0x1400015ff58 HELLO
5 0x1400015ff58 HELLO
6 0x140001dff58 HELLO <- CHANGED
7 0x140001dff58 HELLO
8 0x140001dff58 HELLO
9 0x140001dff58 HELLO
*/
