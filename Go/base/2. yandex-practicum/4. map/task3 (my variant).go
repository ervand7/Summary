package main

import "fmt"

// RemoveDuplicates_ Напишите функцию, которая убирает дубликаты, сохраняя порядок слайса:
func RemoveDuplicates_(input []string) []string {
	tempMap := make(map[string]int)
	var result []string
	for _, value := range input {
		if _, ok := tempMap[value]; !ok {
			tempMap[value] = 1
			result = append(result, value)
		}
	}
	return result
}

func main() {
	input := []string{
		"cat",
		"dog",
		"bird",
		"dog",
		"parrot",
		"cat",
	}
	fmt.Println(input)                    // [cat dog bird dog parrot cat
	fmt.Println(RemoveDuplicates_(input)) // [cat dog bird parrot]
	fmt.Println(input)                    // [cat dog bird dog parrot cat]
}
