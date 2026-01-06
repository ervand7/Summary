package main

import "fmt"

/*
Предположим, что есть два типа компьютеров: Mac и Windows — и два
типа принтеров: Epson и HP. Можно создать четыре структуры для
всех комбинаций, а можно применить паттерн Мост и создать две иерархии:
иерархию абстракции, куда входят компьютеры;
иерархию реализации, которая включает принтеры.
Эти иерархии будут общаться через Мост, в котором компьютер содержит
ссылку на принтер. Компьютеры и принтеры можно реализовывать отдельно,
независимо друг от друга.
*/

// Computer — абстракция компьютера.
type Computer interface {
	Print()
	SetPrinter(Printer)
}

// Mac — компьютер Mac.
type Mac struct {
	printer Printer
}

func (m *Mac) Print() {
	fmt.Println("Печать для Mac.")
	m.printer.PrintFile()
}

func (m *Mac) SetPrinter(p Printer) {
	m.printer = p
}

// Windows — компьютер Windows.
type Windows struct {
	printer Printer
}

func (w *Windows) Print() {
	fmt.Println("Печать для Windows.")
	w.printer.PrintFile()
}

func (w *Windows) SetPrinter(p Printer) {
	w.printer = p
}

// Printer — интерфейс для принтера.
type Printer interface {
	PrintFile()
}

type Epson struct {
}

func (p *Epson) PrintFile() {
	fmt.Println("Печать на принтере Epson.")
}

type HP struct {
}

func (p *HP) PrintFile() {
	fmt.Println("Печать на принтере HP.")
}

func main() {
	// создаём два принтера
	hp := &HP{}
	epson := &Epson{}

	// печать на Mac
	mac := &Mac{}
	mac.SetPrinter(hp)
	mac.Print()
	mac.SetPrinter(epson)
	mac.Print()

	// печать на Windows
	win := &Windows{}
	win.SetPrinter(hp)
	win.Print()
	win.SetPrinter(epson)
	win.Print()
}

/*
Печать для Mac.
Печать на принтере HP.
Печать для Mac.
Печать на принтере Epson.
Печать для Windows.
Печать на принтере HP.
Печать для Windows.
Печать на принтере Epson.
*/
