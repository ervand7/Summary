package main

import "fmt"

func main() {
	first := &SingleList{}
	first.AddHead(1)
	first.AddHead(2)
	first.AddHead(3)
	first.AddHead(4)

	first.Head.Traverse()
	first.Reverse()
	fmt.Println()
	first.Head.Traverse()
}

// SingleList список, внутри которого будут ноды
type SingleList struct {
	Len  int
	Head *ListNode
}

// ListNode нода
type ListNode struct {
	val  int
	next *ListNode
}

// AddHead добавляет новый Head в SingleList
func (s *SingleList) AddHead(num int) {
	newNode := &ListNode{
		val: num,
	}
	if s.Head == nil {
		s.Head = newNode
	} else {
		newNode.next = s.Head
		s.Head = newNode
	}
	s.Len++
}

// Traverse обходит все элементы списка SingleList и печатает каждый
func (l *ListNode) Traverse() {
	for l != nil {
		fmt.Println(l.val)
		l = l.next
	}
}

// Reverse Меняет Head'ы у нод
func (s *SingleList) Reverse() {
	curr := s.Head
	var prev *ListNode
	var next *ListNode

	for curr != nil {
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	}
	s.Head = prev
}
