package main

import "fmt"

// TableMaker — интерфейс для столиков
type TableMaker interface {
	SetStyle(string)
	SetWood(string)
	GetData() string
}

// Table — абстрактный столик
type Table struct {
	Style string
	Wood  string
}

func (t *Table) SetStyle(style string) {
	t.Style = style
}

func (t *Table) SetWood(wood string) {
	t.Wood = wood
}

func (t *Table) GetData() string {
	return fmt.Sprintf("Столик [Стиль: %s, Дерево: %s]", t.Style, t.Wood)
}

// Factory — абстрактная фабрика
type Factory interface {
	MakeTable(string) TableMaker
}

// ArtDeco — фабрика ар-деко
type ArtDeco struct {
}

func (a *ArtDeco) MakeTable(wood string) TableMaker {
	var table Table
	table.SetStyle("ар-деко")
	table.SetWood(wood)
	return &table
}

// Modern — фабрика модерна
type Modern struct {
}

func (m *Modern) MakeTable(wood string) TableMaker {
	var table Table
	table.SetStyle("модерн")
	table.SetWood(wood)
	return &table
}

// GetFactory — фабричный метод
func GetFactory(style string) Factory {
	if style == "art-deco" {
		return &ArtDeco{}
	}
	if style == "modern" {
		return &Modern{}
	}
	return nil
}

func main() {
	factory1 := GetFactory("art-deco")
	table := factory1.MakeTable("дуб")
	fmt.Println(table.GetData()) // Столик [Стиль: ар-деко, Дерево: дуб]

	factory2 := GetFactory("modern")
	table = factory2.MakeTable("ясень")
	fmt.Println(table.GetData()) // Столик [Стиль: модерн, Дерево: ясень]
}
