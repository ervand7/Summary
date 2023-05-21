package person

// Person структура, описывающая человека
type Person struct {
	name     string
	homework string
	children []*Person
}

// DoHomework — делает домашнюю работу
func (p Person) DoHomework() string {
	return p.homework
}

// Children — сообщает информацию о детях
func (p Person) Children() []*Person {
	return p.children
}

// Work — выполняет поручения на работе
func (p Person) Work(tasks []string) string {
	s := p.name + "Person work:"
	for _, task := range tasks {
		s += "\n I do " + task
	}
	return s
}

// String — сообщает информацию о себе
func (p Person) String() string {
	return p.name
}
