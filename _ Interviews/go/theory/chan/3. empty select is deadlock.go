package main

// empty select is deadlock

func main() {
	select {}
}
