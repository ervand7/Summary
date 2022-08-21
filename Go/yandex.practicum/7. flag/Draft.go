package main

import "flag"

func main() {
	ptr := flag.String("flag1", "foo", "string1")
	flag.StringVar(ptr, "flag2", "bar", "string2")
	flag.StringVar(ptr, "flag3", "bazz", "string2")
	flag.Parse()
}
