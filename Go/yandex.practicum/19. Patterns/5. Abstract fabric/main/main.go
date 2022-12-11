package main

import "fmt"

func main() {
	artdecoFactory := GetFactory("art-deco")
	modernFactory := GetFactory("modern")

	artdecoChair := artdecoFactory.MakeChair("дуб")
	artdecoTable := artdecoFactory.MakeTable("дуб")

	modernChair := modernFactory.MakeChair("ясень")
	modernTable := modernFactory.MakeTable("ясень")

	fmt.Println(artdecoChair.Print(), artdecoTable.Print())
	fmt.Println(modernChair.Print(), modernTable.Print())
}
