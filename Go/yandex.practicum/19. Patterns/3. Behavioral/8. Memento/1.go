package main

import "fmt"

/*
Шаблон Хранитель позволяет зафиксировать и сохранить состояние объекта,
чтобы иметь возможность потом восстановить это состояние. Так можно
реализовывать Undo-операции, вести историю состояний объекта, путешествовать
по этой истории, строить и анализировать трассу состояний.
Паттерн Хранитель используется, когда:
 - нужно сохранить состояние объекта, чтобы была возможность вернуть объект
к этому состоянию в будущем;
 - нужно скрыть приватные поля при сохранении состояния: шаблон предполагает,
что сам объект сделает снимок состояния.
В классической формулировке шаблон подразумевает три сущности:
 - originator — объект, состояния которого интересны разработчику;
 - memento — снимок состояния;
 - caretaker — объект, который может хранить снимок и вернуть его объекту
originator для восстановления состояния.
Объект caretaker не знает внутреннее устройство memento, не умеет с
ним работать и не должен его менять. Сделать свой снимок и восстановить
состояние по этому снимку может только originator.
Абстрактный пример на Go может выглядеть так:
*/

type originator struct {
	state string
}

// createMemento создаёт снимок состояния объекта.
func (o *originator) createMemento() *memento {
	return &memento{state: o.state}
}

// restoreMemento восстанавливает состояние объекта.
func (o *originator) restoreMemento(m *memento) {
	o.state = m.getSavedState()
}

func (o *originator) doSomething(s string) {
	o.state = s
}

func (o *originator) getState() string {
	return o.state
}

type memento struct {
	state string
}

func (m *memento) getSavedState() string {
	return m.state
}

type caretaker struct {
	mementos []*memento
}

// addMemento добавляет снимок состояния.
func (c *caretaker) addMemento(m *memento) {
	c.mementos = append(c.mementos, m)
}

// getMemento возвращает снимок состояния.
func (c *caretaker) getMemento(index int) *memento {
	return c.mementos[index]
}

func main() {
	caretaker := &caretaker{
		mementos: make([]*memento, 0),
	}
	originator := &originator{
		state: "A",
	}

	fmt.Printf("Current state: %s\n", originator.getState())
	caretaker.addMemento(originator.createMemento())

	originator.doSomething("B")
	fmt.Printf("Current state: %s\n", originator.getState())
	caretaker.addMemento(originator.createMemento())

	originator.doSomething("C")
	fmt.Printf("Current state: %s\n", originator.getState())
	caretaker.addMemento(originator.createMemento())

	// восстанавливаем состояния
	originator.restoreMemento(caretaker.getMemento(1))
	fmt.Printf("Restored to: %s\n", originator.getState())

	originator.restoreMemento(caretaker.getMemento(0))
	fmt.Printf("Restored to: %s\n", originator.getState())
}

/*
Current state: A
Current state: B
Current state: C
Restored to: B
Restored to: A
*/
