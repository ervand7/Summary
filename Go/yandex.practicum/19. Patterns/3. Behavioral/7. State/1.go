package main

import (
	"fmt"
	"unicode"
)

type TokenType int

const (
	TNumber = iota
)

const (
	StateMain = iota
	StateNumber
)

// Token — информация о токене.
type Token struct {
	Type  TokenType
	Value string
}

// State — интерфейс состояния. Next передаёт очередной символ.
// Если символ разобран, то возвращается true.
type State interface {
	Next(rune) bool
}

// Number определяет число.
type Number struct {
	buf   []rune
	lexer *Lexer
}

func (l *Number) Next(r rune) bool {
	if unicode.IsDigit(r) {
		l.buf = append(l.buf, r)
		return true
	}
	l.lexer.NewToken(TNumber, l.buf)
	l.lexer.SetState(StateMain)
	l.buf = l.buf[:0]
	return false
}

// Main — состояние по умолчанию.
type Main struct {
	lexer *Lexer
}

func (l *Main) Next(r rune) bool {
	if unicode.IsDigit(r) {
		l.lexer.SetState(StateNumber)
		return false
	}
	return true
}

// Lexer содержит список состояний и полученные токены.
type Lexer struct {
	states []State
	state  State
	tokens []Token
}

// SetState изменяет состояние.
func (lex *Lexer) SetState(state int) {
	if state >= len(lex.states) {
		panic("unknown state")
	}
	lex.state = lex.states[state]
}

// NewToken добавляет токен.
func (lex *Lexer) NewToken(t TokenType, value []rune) {
	lex.tokens = append(lex.tokens, Token{
		Type:  t,
		Value: string(value),
	})
}

func main() {
	var lex Lexer

	// определяем состояния
	lex.states = []State{&Main{lexer: &lex}, &Number{lexer: &lex}}
	lex.SetState(StateMain)

	// пробуем разобрать эту строку
	s := "line778, 5 + 35 равно 40"
	for _, ch := range s {
		for !lex.state.Next(ch) {
		}
	}
	// завершаем разбор последнего токена, если он начат
	lex.state.Next(0)

	fmt.Println(lex.tokens)
}
