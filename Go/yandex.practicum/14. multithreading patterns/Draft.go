package main

import "fmt"

func CheckArrayElems(arr map[string]string) {
	for key, val := range arr {
		if len(val) == 5 {
			arr[key] = "hello" + "/" + val
		}
	}
}

func main() {
	arr := map[string]string{"qwert": "qwert", "wert1": "qwert", "wert2": "qwert", "wert3": "qwert", "wert4": "qwert"}
	CheckArrayElems(arr)
	fmt.Println(arr)

}
