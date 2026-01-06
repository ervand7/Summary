package main

import "fmt"

/*
Яркий пример применения шаблона в Go — цепочка middleware-обработчиков
http.Request, которую можно реализовать самостоятельно или взять
из сторонних HTTP-фреймворков.
А вот абстрактный пример классической реализации шаблона:
*/

// Processor — интерфейс обработчика.
type Processor interface {
	Process(Request)
	SetNext(Processor)
}

type Kind int

const (
	Urgent Kind = 1 << iota
	Special
	Valuable
)

// Request описывает поля запроса.
type Request struct {
	Kind Kind
	Data string
}

// Printer — обработчик.
type Printer struct {
	next Processor
}

func (p *Printer) Process(r Request) {
	fmt.Printf("Printer: %s\n", r.Data)
	if p.next != nil {
		p.next.Process(r)
	}
}

func (p *Printer) SetNext(next Processor) {
	p.next = next
}

// Saver — обработчик.
type Saver struct {
	next Processor
}

func (s *Saver) Process(r Request) {
	if r.Kind&(Valuable|Special) != 0 {
		fmt.Printf("Saver: %s\n", r.Data)
	}
	if s.next != nil {
		s.next.Process(r)
	}
}

func (s *Saver) SetNext(next Processor) {
	s.next = next
}

// Logger — обработчик.
type Logger struct {
	next Processor
}

func (l *Logger) Process(r Request) {
	if r.Kind&Urgent != 0 {
		fmt.Printf("Logger: %s\n", r.Data)
	}
	if l.next != nil {
		l.next.Process(r)
	}
}

func (l *Logger) SetNext(next Processor) {
	l.next = next
}

func main() {
	l := new(Logger)
	p := new(Printer)
	l.SetNext(p)
	s := new(Saver)
	s.SetNext(l)
	s.Process(Request{0, "Average"})
	// Printer: Average
	s.Process(Request{Valuable, "Do not forget"})
	// Saver: Do not forget
	// Printer: Do not forget
	s.Process(Request{Urgent | Special, "Alert!!!"})
	// Saver: Alert!!!
	// Logger: Alert!!!
	// Printer: Alert!!!
}
