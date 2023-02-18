package main

import (
	"fmt"
	"net"
)

func main() {
	fmt.Println(net.LookupAddr("157.240.9.35"))
}
