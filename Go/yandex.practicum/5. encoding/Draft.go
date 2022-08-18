package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	var v interface{}
	err := json.Unmarshal([]byte(`[0, 10, 30]`), &v)
	fmt.Printf("%T, %[1]v, %v", v, err)
}
