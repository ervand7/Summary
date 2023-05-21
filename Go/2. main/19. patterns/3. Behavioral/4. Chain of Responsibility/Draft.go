package main

import "fmt"

func main() {
	type Kind int

	const (
		qwe Kind = 2 << iota
		wer
		ert
		rty
		tyu
		yui
		zxc
		cxv
		cvb
		bvn
	)

	fmt.Println(wer, ert, rty, tyu, yui, zxc, cxv, cvb, bvn)
}

// 2 4 8 16 32 64 128 256 512
