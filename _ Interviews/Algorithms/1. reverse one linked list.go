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

	var prev *ListNode // temp
	var curr = s.Head  // temp курсор с тем же адресом, что и Head
	var next *ListNode // temp

	for curr != nil {
		next = curr.next // temp next будет ссылаться на тот же адрес, что и узел.next
		curr.next = prev // присваиваем узел.next значение из prev
		prev = curr      // сдвигаем temp curr на temp prev
		curr = next      // сдвигаем temp next на temp curr
	}
	s.Head = prev
}
