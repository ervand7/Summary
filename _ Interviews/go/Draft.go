package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 88, 77}
	bubbleSort(a)
	fmt.Println(a)
}

func sayHello() {
	fmt.Println("Hello")
}

func calcSumOfIntegers(a, b int) int {
	return a + b
}

func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

func bfs(graph map[string][]string, start string, end string) bool {
	queue := graph[start]
	checked := make(map[string]bool)
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		if !checked[node] {
			if node == end {
				return true
			}
			queue = append(queue, graph[node]...)
			checked[node] = true
		}
	}
	return false
}

func bubbleSort(arr []int) {
	for i := 0; i < len(arr)-1; i++ {
		for j := 1; j < len(arr)-i; j++ {
			if arr[j-1] > arr[j] {
				swap(arr, j)
			}
		}
	}
}

func swap(arr []int, j int) {
	arr[j-1], arr[j] = arr[j], arr[j-1]
}

func prefixFunction(pattern string) []int {
	prefix := make([]int, len(pattern))
	j := 0
	for i := 1; i < len(pattern); i++ {
		for j > 0 && pattern[i] != pattern[j] {
			j = prefix[j-1]
		}
		if pattern[i] == pattern[j] {
			j++
		}
		prefix[i] = j
	}
	return prefix
}

func kmpSearch(text string, pattern string) int {
	prefix := prefixFunction(pattern)
	j := 0
	for i := 0; i < len(text); i++ {
		for j > 0 && text[i] != pattern[j] {
			j = prefix[j-1]
		}
		if text[i] == pattern[j] {
			j++
		}
		if j == len(pattern) {
			return i - j + 1
		}
	}
	return -1
}
