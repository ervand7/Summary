package main

import (
	"errors"
)

type Storage map[string]string

func (s Storage) Get(key string) (string, error) {
	// обрабатываем ошибку
	if val, ok := s[key]; ok {
		return val, nil
	}
	return "", errors.New("Not found key " + key)
}
