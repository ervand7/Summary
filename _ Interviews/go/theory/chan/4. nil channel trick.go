package main

func main() {
	var ch chan int // nil
	
	<-ch // blocks forever
}
