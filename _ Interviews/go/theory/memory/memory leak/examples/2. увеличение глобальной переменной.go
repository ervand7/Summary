package main

import "time"

var globalSlice = make([]int64, 0)

func appendSlice() {
	globalSlice = append(globalSlice, time.Now().Unix())
}
