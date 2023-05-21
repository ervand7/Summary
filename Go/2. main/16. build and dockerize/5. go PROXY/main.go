package main

import (
	"fmt"
)

var version string = "debug"

func main() {
	fmt.Printf("the current version is %s\n", version)
	// ctx := context.WithValue(context.Background(), "version", version)
	// и далее уже передаем этот контекст, например, в логи

}

// $ go build -ldflags="-X 'main.version=v1.0.0'" -o my_binary && ./my_binary
// output: the current version is v1.0.0
