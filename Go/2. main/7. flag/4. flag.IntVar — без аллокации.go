package main

import (
	"flag"
	"fmt"
)

func main() {
	var config struct {
		host string
		port int
	}
	// связывать так
	flag.IntVar(&config.port, "port", 8080, "port to listen on")
	flag.StringVar(&config.host, "host", "localhost", "host to listen on")

	flag.Parse()
	fmt.Println(config.port)
	fmt.Println(config.host)
}

/*
1) go run 4.\ flag.IntVar\ —\ без\ аллокации.go --help
Usage of /var/folders/ky/889zsrl12nvcz0x0wdr24hsm0000gn/T/go-build255945262/b001/exe/4. flag.IntVar — без аллокации:
  -host string
        host to listen on (default "localhost")
  -port int
        port to listen on (default 8080)

2) $ go run 4.\ flag.IntVar\ —\ без\ аллокации.go --port=5000 --host 129.3.554.3.11
5000
129.3.554.3.11
*/
