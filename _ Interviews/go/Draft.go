package main

import (
	"encoding/json"
	"fmt"
	"time"
)

type Person struct {
	Name        string    `json:"name"`
	DateOfBirth time.Time `json:"date_of_birth"`
}

func main() {
	// here date_of_birth is in not standard RFC1123Z format
	raw := `{"name":"John Doe","date_of_birth":"Sat, 04 Nov 1923 22:11:08 +0100"}`
	// create temporary struct where DateOfBirth field will be string, not time.Time
	temp := struct {
		// use embedding
		Person
		// this will overlap Person.DateOfBirth
		DateOfBirth string `json:"date_of_birth"`
	}{}
	// unmarshal into temp struct
	err := json.Unmarshal([]byte(raw), &temp)
	if err != nil {
		fmt.Println(err.Error())
	}

	// parse not standard RFC1123Z time format
	dateOfBirth, err := time.Parse(time.RFC1123Z, temp.DateOfBirth)
	if err != nil {
		fmt.Println(err.Error())
	}

	// and build final result from temp
	result := Person{
		Name:        temp.Name,
		DateOfBirth: dateOfBirth,
	}

	fmt.Printf("%#v", result)
}

// {John Doe 1923-11-04 22:11:08 +0100 CET}
