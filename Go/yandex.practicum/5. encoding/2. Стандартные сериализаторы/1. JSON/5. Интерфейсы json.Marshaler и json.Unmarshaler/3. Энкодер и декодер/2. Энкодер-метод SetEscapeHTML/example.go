package main

import (
	"bytes"
	"encoding/json"
	"fmt"
)

func main() {
	v := struct {
		Url string
	}{
		Url: "http://mysite.com?id=1234&param=2",
	}
	buf := bytes.NewBuffer([]byte{})
	encoder := json.NewEncoder(buf)
	encoder.SetEscapeHTML(false) // без этой опции символ '&' будет заменён на "\u0026"
	encoder.Encode(v)
	fmt.Println(buf.String()) // {"Url":"http://mysite.com?id=1234&param=2"}

}
