package main

import "fmt"

// Pizza — интерфейс со стоимостью пиццы в рублях.
type Pizza interface {
	GetCost() int
}

// DefaultPizza — пицца по умолчанию.
type DefaultPizza struct {
}

func (p *DefaultPizza) GetCost() int {
	return 500
}

// TomatoPizza — пицца с помидорами.
type TomatoPizza struct {
	Pizza Pizza
}

func (p *TomatoPizza) GetCost() int {
	return p.Pizza.GetCost() + 40 // добавляем стоимость
}

// CheesePizza — пицца с сыром.
type CheesePizza struct {
	Pizza Pizza
}

func (p *CheesePizza) GetCost() int {
	return p.Pizza.GetCost() + 60 // добавляем стоимость
}

func main() {
	pizza := &DefaultPizza{}

	// добавляем помидоры
	pizzaTomato := &TomatoPizza{
		Pizza: pizza,
	}

	// добавляем сыр
	pizzaCheeseTomato := &CheesePizza{
		Pizza: pizzaTomato,
	}

	fmt.Printf(
		"Пицца с помидорами и сыром стоит %d руб.\n",
		pizzaCheeseTomato.GetCost(),
	)
}

// Пицца с помидорами и сыром стоит 600 руб.
