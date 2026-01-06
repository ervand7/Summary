package main

/*
We could just create one overloaded interface and place
Save, LogSomething, Greet in it. But that would violate
interface segregation principle.
*/

type Saver interface {
	Save(data string) error
}

type Logger interface {
	LogSomething(message string)
}

type Speaker interface {
	Greet() (greeting string)
}
