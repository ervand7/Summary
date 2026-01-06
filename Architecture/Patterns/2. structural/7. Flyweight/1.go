package main

import (
	"fmt"
	"strings"
)

const (
	AttackEquipType  = "attackEquip"
	DefenseEquipType = "defenseEquip"
)

type Equip interface {
	GetColor() string
}

var (
	// вся экипировка будет храниться в объекте-одиночке equipFactory
	equipFactory = &EquipFactory{
		equipMap: make(map[string]Equip),
	}
)

type EquipFactory struct {
	equipMap map[string]Equip
}

func (d *EquipFactory) String() string {
	var s strings.Builder

	for equipType, equip := range d.equipMap {
		fmt.Fprintf(&s, "Экипировка — Тип: %s Цвет: %s\n", equipType, equip.GetColor())
	}
	return s.String()
}

// GetEquipByType возвращает существующую экипировку или создаёт новую.
func (d *EquipFactory) GetEquipByType(equipType string) Equip {
	eq, ok := d.equipMap[equipType]
	if ok {
		return eq
	}

	switch equipType {
	case AttackEquipType:
		eq = NewAttackEquip()
	case DefenseEquipType:
		eq = NewDefenseEquip()
	default:
		panic(fmt.Errorf("Неизвестный тип экипировки: %s", equipType))
	}
	d.equipMap[equipType] = eq
	return eq
}

// AttackEquip — экипировка для нападающих.
type AttackEquip struct {
	color string
}

func (t *AttackEquip) GetColor() string {
	return t.color
}

func NewAttackEquip() *AttackEquip {
	return &AttackEquip{color: "red"}
}

// DefenseEquip — экипировка для обороняющихся.
type DefenseEquip struct {
	color string
}

func (c *DefenseEquip) GetColor() string {
	return c.color
}

func NewDefenseEquip() *DefenseEquip {
	return &DefenseEquip{color: "blue"}
}

// Player — объект для игрока.
type Player struct {
	equip      Equip  // экипировка
	playerType string // тип игрока
	lat        int    // координаты
	long       int
}

func NewPlayer(playerType, equipType string) *Player {
	equip := equipFactory.GetEquipByType(equipType)
	return &Player{
		playerType: playerType,
		equip:      equip,
	}
}

func (p *Player) SetLocation(lat, long int) {
	p.lat = lat
	p.long = long
}

// Game — главная структура игры с набором игроков.
type Game struct {
	Attack  []*Player
	Defense []*Player
}

func NewGame() *Game {
	return &Game{
		Attack:  make([]*Player, 0),
		Defense: make([]*Player, 0),
	}
}

// AddAttack добавляет нападающего игрока.
func (g *Game) AddAttack(equipType string) {
	g.Attack = append(g.Attack, NewPlayer("Attack", equipType))
}

// AddDefense добавляет обороняющегося игрока.
func (g *Game) AddDefense(equipType string) {
	g.Defense = append(g.Defense, NewPlayer("Defense", equipType))
}

func main() {
	game := NewGame()

	// добавляем нападающих
	game.AddAttack(AttackEquipType)
	game.AddAttack(AttackEquipType)
	game.AddAttack(AttackEquipType)
	game.AddAttack(AttackEquipType)

	// добавляем обороняющихся
	game.AddDefense(DefenseEquipType)
	game.AddDefense(DefenseEquipType)
	game.AddDefense(DefenseEquipType)

	// выводим количество объектов с экипировкой
	fmt.Println(equipFactory)
}

/*
Экипировка — Тип: attackEquip Цвет: red
Экипировка — Тип: defenseEquip Цвет: blue
*/
