package main

import (
	"encoding/xml"
	"fmt"
	"log"
)

/*
Определите XML-теги полей Person и List так, чтобы программа выводила:
1 Carla Mitchel  [123-45-67 890-12-34]
2 Michael Smith msmith@example.com []
*/

type Person struct {
	ID     int `xml:"id,attr"`
	Name   string
	Email  string
	Phones []string `xml:"Phones>Phone"`
}

type List struct {
	Persons []Person `xml:"Person"`
}

func main() {
	var v List
	data := `
    <List>
        <Person id="1">
            <Name>Carla Mitchel</Name>
            <Phones>
                <Phone>123-45-67</Phone>
                <Phone>890-12-34</Phone>
            </Phones>
        </Person>
        <Person id="2">
            <Name>Michael Smith</Name>
            <Email>msmith@example.com</Email>
        </Person>
    </List>
    `
	err := xml.Unmarshal([]byte(data), &v)
	if err != nil {
		log.Fatal(err)
	}
	for _, item := range v.Persons {
		fmt.Println(item.ID, item.Name, item.Email, item.Phones)
	}
}
