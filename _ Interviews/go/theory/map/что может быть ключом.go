package main

func main() {
	var _ map[struct{}]int
	var _ map[int]int
	var _ map[string]int
	var _ map[[4]int]int
	var _ map[rune]int
	var _ map[byte]int
	var _ map[float32]int
	var _ map[float64]int
	var _ map[error]int
	var _ map[any]int
	var _ map[interface{}]int
	var _ map[*any]int
	var _ map[*func()]int
	var _ map[chan any]int
	var _ map[*map[int]int]int
}
