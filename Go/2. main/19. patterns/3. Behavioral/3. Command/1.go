package main

import "fmt"

// интерфейсы
type command interface {
	execute()
}

type receiver interface {
	action()
}

type invoker struct {
	commands map[string]command
}

func newInvoker() *invoker {
	i := new(invoker)
	i.commands = make(map[string]command)
	return i
}

func (i *invoker) do(c string) {
	i.commands[c].execute()
}

// реализация command
type printer struct {
	receiver receiver
}

func (c *printer) execute() {
	c.receiver.action()
}

type rcvr struct {
	name string
}

func (r *rcvr) action() {
	fmt.Println(r.name)
}

func main() {
	var rcvr1 = rcvr{"John Doe"}
	var cmd1 = printer{&rcvr1}
	var rcvr2 = rcvr{"Hello, world!"}
	var cmd2 = printer{&rcvr2}
	invkr := newInvoker()
	invkr.commands["print_name"] = &cmd1
	invkr.commands["print_hello"] = &cmd2
	// собственно применение команд
	invkr.do("print_name")
	invkr.do("print_hello")
}

/*
John Doe
Hello, world!
*/
