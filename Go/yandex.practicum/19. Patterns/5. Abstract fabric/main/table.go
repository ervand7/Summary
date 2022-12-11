package main

import "fmt"

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

func (t *Table) Print() string {
	return fmt.Sprintf("Столик [Стиль: %s, Дерево: %s]", t.Style, t.Wood)
}
