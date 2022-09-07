package main

import (
	"encoding/hex"
	"fmt"
)

func main() {
	//Storage := make(map[string]map[string]string, 0)
	//Storage["123e4567-e89b-12d3-a456-426614174000"] = map[string]string{"http": "http"}
	////Storage["qwe"]["xc"] = "eeeeeee"
	//fmt.Println(Storage)
	//
	//type ShortenURLStruct struct {
	//	ShortenURL string
	//	OriginUrl  string
	//	UserID     string
	//}
	//Storage2 := make(map[string]ShortenURLStruct, 0)
	//Storage2["hello"] = ShortenURLStruct{
	//	ShortenURL: "http",
	//	OriginUrl:  "http//",
	//	UserID:     "123",
	//}
	//fmt.Println(Storage2["1"].UserID)

	str := "Hello"
	dst := make([]byte, 0)
	hex.Decode(dst, []byte(str))
	fmt.Println(dst)
}
