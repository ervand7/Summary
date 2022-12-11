package main

import (
	"fmt"
	"strings"
)

/*
Фабрика (фабричный метод) — это порождающий паттерн проектирования, который определяет
интерфейс для создания объектов определённого типа. Паттерн предлагает создавать
объекты не напрямую, а через вызов специального фабричного метода.
Все объекты должны иметь общий интерфейс, который отвечает за их создание.

При использовании в объектно-ориентированном программировании базовый класс
делегирует создание объектов классам-наследникам.
Так как в Go отсутствуют классы и наследование, нельзя реализовать
классический вариант Фабрики.
Паттерн используется, когда заранее неизвестны типы объектов
*/

type DatabaseConnector interface {
	Query(q string) error
}

type MysqlConnector struct {
}

func newMysqlConnector(dsn string) *MysqlConnector {
	fmt.Println("Connect to mysql")
	return &MysqlConnector{}
}

func (c *MysqlConnector) Query(q string) error {
	fmt.Printf("Query to mysql: %s\n", q)
	return nil
}

type PostgresqlConnector struct {
}

func newPostgresqlConnector(dsn string) *PostgresqlConnector {
	fmt.Println("Connect to postgresql")
	return &PostgresqlConnector{}
}

func (c *PostgresqlConnector) Query(q string) error {
	fmt.Printf("Query to postgresql: %s\n", q)
	return nil
}

// NewConnector реализует фабричный метод
func NewConnector(dsn string) DatabaseConnector {
	switch {
	case strings.HasPrefix(dsn, "mysql://"):
		return newMysqlConnector(dsn)
	case strings.HasPrefix(dsn, "postgresql://"):
		return newPostgresqlConnector(dsn)
	default:
		panic(fmt.Sprintf("unknown dsn protocol: %s", dsn))
	}
}

func main() {
	mysql := NewConnector("mysql://...")
	mysql.Query("SELECT something FROM list")
	// Connect to mysql
	// Query to mysql: SELECT something FROM list

	pg := NewConnector("postgresql://...")
	pg.Query("SELECT something FROM list")
	// Connect to postgresql
	// Connect to postgresql
}
