package main

import (
	"sync"
	"sync/atomic"
)

type Freq struct {
	// частотная мапа, хранящая вес ключей
	// для ключей будем использовать string
	// для значений — *int64
	*sync.Map
}

// Increment метод корректно увеличивает значение ключа при конкурентном доступе
func (f Freq) Increment(key string, value int64) {
	// если ключа ещё нет в мапе, то записываем со значением &value
	count, loaded := f.LoadOrStore(key, &value)
	// а если ключ уже есть,
	if loaded {
		// то атомарно увеличиваем значение
		atomic.AddInt64(count.(*int64), value)
	}
}
