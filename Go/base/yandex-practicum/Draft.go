package main

import (
	"fmt"
	"net/url"
)

func someURL() string {
	url_ := url.URL{
		Scheme: "https",
		Host:   "example.com",
	}
	return url_.String()
}

func main() {
	fmt.Println(someURL())
}
