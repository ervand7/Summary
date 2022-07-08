package main

import (
	"fmt"
)

// Person — структура, описывающая человека.
type Person struct {
	Name string
	Year int
}

// NewPerson возвращает новую структуру Person.
func NewPerson(name string, year int) Person {
	return Person{
		Name: name,
		Year: year,
	}
}

// String возвращает информацию о человеке.
func (p Person) String() string {
	return fmt.Sprintf("Имя: %s, Год рождения: %d", p.Name, p.Year)
}

// Print выводит информацию о человеке.
func (p Person) Print() {
	fmt.Println(p.String())
}

// Student описывает студента с использованием вложенной
// структуры Person. То есть структура Student описывает.
type Student struct {
	Person // вложенный объект Person
	Group  string
}

func NewStudent(name string, year int, group string) Student {
	return Student{
		Person: NewPerson(name, year), // Явно создаём структуру Person
		Group:  group,
	}
}

// String возвращает информацию о студенте.
func (s Student) String() string {
	return fmt.Sprintf("%s, Группа: %s", s.Person, s.Group)
}

func main() {
	s := NewStudent("John Doe", 1980, "701")
	s.Print()                            // Имя: John Doe, Год рождения: 1980
	fmt.Println(s)                       // Имя: John Doe, Год рождения: 1980, Группа: 701
	fmt.Println(s.Name, s.Year, s.Group) // John Doe 1980 701
}
