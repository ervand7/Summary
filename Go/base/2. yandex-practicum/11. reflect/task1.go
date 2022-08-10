package main

/*
Представьте что вы разрабатываете многопользовательскую игру.
Игровая логика обсчитывается на сервере, реализованном на Go.

В какой-то момент от дизайнеров поступает запрос внедрения для
игроков массовых заклинаний. То есть заклинание должно действовать на множество
объектов, имеющих разнообразную структуру и типы. Тут вы понимаете,
что переписывать все типы и реализовывать для каждого интерфейс
CastReceiver слишком сложная задача.

Реализуйте применение заклинаний с помощью рефлексии.
Каждое заклинание удовлетворяет интерфейсу Spell — можно узнать,
на какую характеристику объекта и на какую величину оно влияет.
*/

import (
	"fmt"
	"log"
	"reflect"
)

type Spell interface {
	// Name название заклинания
	Name() string
	// Char характеристика, на которую воздействует
	Char() string
	// Value количественное значение
	Value() int
}

type spell struct {
	name string
	char string
	val  int
}

func newSpell(name string, char string, val int) Spell {
	return &spell{name: name, char: char, val: val}
}

func (s spell) Name() string {
	return s.name
}

func (s spell) Char() string {
	return s.char
}

func (s spell) Value() int {
	return s.val
}

type Zombie struct {
	Health int
}

type Daemon struct {
	Health int
}

type Orc struct {
	Health int
}

type Wall struct {
	Durability int
}

type Player struct {
	name   string
	health int
}

// CastReceiver — если объект удовлетворяет этом интерфейсу,
// то заклинание применяется через него, а не каким-либо другим путем.
// И из всех персонажей, только player удовлетворяет этому интерфейсу
type CastReceiver interface {
	ReceiveSpell(s Spell)
}

func (p *Player) ReceiveSpell(s Spell) {
	if s.Char() == "Health" {
		p.health += s.Value()
	}
}

func CastToAll(spell Spell, objects []interface{}) {
	for _, obj := range objects {
		CastTo(spell, obj)
	}
}

// CastTo реализуйте эту функцию.
func CastTo(spell Spell, object interface{}) {
	if recv, ok := object.(CastReceiver); ok {
		recv.ReceiveSpell(spell)
		return
	}

	// проверяем, что переданный объект указатель на структуру
	val := reflect.ValueOf(object)
	if val.Kind() != reflect.Ptr || val.Elem().Kind() != reflect.Struct {
		return
	}

	// ищем в структуре нужную характеристику
	field := val.Elem().FieldByName(spell.Char())
	// не нашли
	if !field.IsValid() {
		return
	}

	// нашли, но изменить её нельзя
	if !field.CanSet() {
		return
	}

	// тип найденного поля не целое число
	if field.Kind() != reflect.Int && field.Kind() != reflect.Int8 &&
		field.Kind() != reflect.Int16 && field.Kind() != reflect.Int32 &&
		field.Kind() != reflect.Int64 {
		return
	}

	field.SetInt(field.Int() + int64(spell.Value()))
	log.Printf("Casted spell %s to %#v", spell.Name(), object)
}

func main() {
	player := &Player{
		name:   "Player_1",
		health: 100,
	}

	enemies := []interface{}{
		&Zombie{Health: 1000},
		&Zombie{Health: 1000},
		&Orc{Health: 500},
		&Orc{Health: 500},
		&Orc{Health: 500},
		&Daemon{Health: 1000},
		&Daemon{Health: 1000},
		&Wall{Durability: 100},
	}

	CastToAll(newSpell("fire", "Health", -50), append(enemies, player))
	CastToAll(newSpell("heal", "Health", 190), append(enemies, player))

	fmt.Printf("%#v", player)
}

/*
2022/07/23 10:45:12 Casted spell fire to &main.Zombie{Health:950}
2022/07/23 10:45:12 Casted spell fire to &main.Zombie{Health:950}
2022/07/23 10:45:12 Casted spell fire to &main.Orc{Health:450}
2022/07/23 10:45:12 Casted spell fire to &main.Orc{Health:450}
2022/07/23 10:45:12 Casted spell fire to &main.Orc{Health:450}
2022/07/23 10:45:12 Casted spell fire to &main.Daemon{Health:950}
2022/07/23 10:45:12 Casted spell fire to &main.Daemon{Health:950}
2022/07/23 10:45:12 Casted spell heal to &main.Zombie{Health:1140}
2022/07/23 10:45:12 Casted spell heal to &main.Zombie{Health:1140}
2022/07/23 10:45:12 Casted spell heal to &main.Orc{Health:640}
2022/07/23 10:45:12 Casted spell heal to &main.Orc{Health:640}
2022/07/23 10:45:12 Casted spell heal to &main.Orc{Health:640}
2022/07/23 10:45:12 Casted spell heal to &main.Daemon{Health:1140}
2022/07/23 10:45:12 Casted spell heal to &main.Daemon{Health:1140}
&main.Player{name:"Player_1", health:240}
*/
