package main

import (
	"fmt"
)

/*
Шаблон Посетитель позволяет отвязать функциональность от объекта.
Новые методы добавляются через промежуточный объект visitor, аккумулирующий
функциональность. Типам семейства добавляется только один метод accept(visitor).
Так проще добавлять операции к существующей базе кода без особых изменений и
страха всё сломать. Этот паттерн чаще всего используется, когда нужно добавить
функционал к объектам разного типа.
Паттерн Посетитель используется, когда:
 - нужно применить одну и ту же операцию к объектам разных типов;
 - часто добавляются новые операции для объектов;
 - требуется добавить новый функционал, но избежать усложнения кода объекта.
Предположим, есть конструктор, который собирает автомобиль из колёс и двигателя.
В какой-то момент нужно добавить тестирование компонентов при сборке.
Рассмотрим, как это можно реализовать, используя паттерн Посетитель.
*/

// CarPart — семейство типов, которым хотим добавить
// функциональность детали автомобиля.
type CarPart interface {
	Accept(CarPartVisitor)
}

// CarPartVisitor — интерфейс visitor,
// в его коде и содержится новая функциональность.
type CarPartVisitor interface {
	testWheel(wheel *Wheel)
	testEngine(engine *Engine)
}

// Wheel — реализация деталей.
type Wheel struct {
	Name string
}

// Accept — единственный метод, который нужно добавить типам семейства,
// ссылка на метод visitor.
func (w *Wheel) Accept(visitor CarPartVisitor) {
	visitor.testWheel(w)
}

type Engine struct{}

func (e *Engine) Accept(visitor CarPartVisitor) {
	visitor.testEngine(e)
}

type Car struct {
	parts []CarPart
}

// NewCar — конструктор автомобиля.
func NewCar() *Car {
	this := new(Car)
	this.parts = []CarPart{
		&Wheel{"front left"},
		&Wheel{"front right"},
		&Wheel{"rear right"},
		&Wheel{"rear left"},
		&Engine{}}
	return this
}

func (c *Car) Accept(visitor CarPartVisitor) {
	for _, part := range c.parts {
		part.Accept(visitor)
	}
}

// TestVisitor — конкретная реализация visitor,
// которая может проверять колёса и двигатель.
type TestVisitor struct {
}

func (v *TestVisitor) testWheel(wheel *Wheel) {
	fmt.Printf("Testing the %v wheel\n", wheel.Name)
}

func (v *TestVisitor) testEngine(engine *Engine) {
	fmt.Println("Testing engine")
}

func main() {
	car := NewCar()
	visitor := new(TestVisitor)
	car.Accept(visitor)
}

/*
Testing the front left wheel
Testing the front right wheel
Testing the rear right wheel
Testing the rear left wheel
Testing engine
*/
