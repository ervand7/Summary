package main

type Set[T comparable] struct {
	m map[T]struct{}
}

func NewSet[T comparable]() *Set[T] {
	return &Set[T]{
		m: map[T]struct{}{},
	}
}

func (s *Set[T]) Add(v T) {
	s.m[v] = struct{}{}
}

func (s *Set[T]) Remove(v T) {
	delete(s.m, v)
}

func (s *Set[T]) Has(v T) bool {
	_, ok := s.m[v]
	return ok
}

func (s *Set[T]) Values() []T {
	var result = make([]T, 0, len(s.m))
	for k := range s.m {
		result = append(result, k)
	}

	return result
}
