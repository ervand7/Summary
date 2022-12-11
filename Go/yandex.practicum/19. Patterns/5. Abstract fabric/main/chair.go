package main

import "fmt"

// Chair — абстрактное кресло
type Chair struct {
	Style string
	Wood  string
}

func (c *Chair) SetStyle(style string) {
	c.Style = style
}

func (c *Chair) SetWood(wood string) {
	c.Wood = wood
}

func (c *Chair) Print() string {
	return fmt.Sprintf("Кресло [Стиль: %s, Дерево: %s]", c.Style, c.Wood)
}
