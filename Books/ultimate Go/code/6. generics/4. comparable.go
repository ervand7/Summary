package main

func index[T comparable](list []T, find T) int {
	for i, v := range list {
		if v == find {
			return i
		}
	}
	return -1
}
