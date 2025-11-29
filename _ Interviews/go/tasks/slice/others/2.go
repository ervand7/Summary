package main

import "fmt"

/*
Because **`b` shares the same underlying array as `a`**.

Steps:
1. `b := a[:2]` → `b` is a view into the same array as `a`.
2. `append(b, 10)` fits into the original array capacity → so it writes **into `a[2]`**.
3. `a[1] = 99` modifies the same shared array.
4. Both slices now reflect the same underlying memory.

That's why:

* `a` becomes: `[1 99 10 4]`
* `b` becomes: `[1 99 10]` (first 3 elements of the same array)

*/

func main() {
	a := []int{1, 2, 3, 4}
	b := a[:2]

	b = append(b, 10)
	a[1] = 99

	fmt.Println("a:", a)
	fmt.Println("b:", b)
}
