package main

import (
	"fmt"
	"strconv"
)

func main() {
	a := make(map[string]string, 0)
	a["hello"] = "world"
	a["hello2"] = "world2"
	fmt.Println(strconv.Itoa(len(a)))

}
