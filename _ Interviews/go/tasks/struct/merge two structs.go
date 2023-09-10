package main

import (
	"fmt"
)

type User struct {
	Id            int
	Name          string
	OfficeId      int
	OfficeAddress string // пусто
}

type Office struct {
	Id      int
	Address string
}

func main() {
	users := []User{
		{
			Id:       1,
			Name:     "User1",
			OfficeId: 1,
		},
		{
			Id:       2,
			Name:     "User2",
			OfficeId: 2,
		},
	}

	offices := []Office{
		{
			Id:      1,
			Address: "Address1",
		},
		{
			Id:      2,
			Address: "Address2",
		},
	}

	hashTable := make(map[int]string)
	for _, off := range offices {
		hashTable[off.Id] = off.Address
	}

	for idx := range users {
		officeID := users[idx].OfficeId
		users[idx].OfficeAddress = hashTable[officeID]
	}

	fmt.Printf("%+v", users)
	// [{Id:1 Name:User1 OfficeId:1 OfficeAddress:Address1} {Id:2 Name:User2 OfficeId:2 OfficeAddress:Address2}]
}
