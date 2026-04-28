package main

import "context"

type Rediser interface {
	Get(ctx context.Context, key string) (string, error)
}

type Service struct {
	partitions []Rediser
}

func (s Service) GetFirst(ctx context.Context, key string) (string, error) {
	// Сделать так, чтобы мы проверили все партиции и ввернули первый результат,
	// который без ошибок. Если все партиции ответили с ошибками, то возвращаем ошибку
	// TODO
}
