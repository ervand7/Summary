package main

// ChairMaker — интерфейс для кресел
type ChairMaker interface {
	SetStyle(string)
	SetWood(string)
	Print() string
}

// TableMaker — интерфейс для столиков
type TableMaker interface {
	SetStyle(string)
	SetWood(string)
	Print() string
}
