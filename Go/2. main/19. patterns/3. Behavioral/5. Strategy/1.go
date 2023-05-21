package main

import "fmt"

/*
Классическая формулировка паттерна включает три типа участников:
 - объект strategy умеет работать с алгоритмами семейства;
 - объекты concreteStrategy содержат частные реализации этих алгоритмов;
 - объект context взаимодействует с клиентским кодом, формирует стратегический запрос.
Приведём пример реализации шаблона с кешированием данных в оперативной памяти.
Поскольку размер памяти ограничен, нужно обеспечить механизм ротации кеша.
При освобождении памяти могут применяться стратегии:
LRU (Least Recently Used) — вычищаем элементы, которые использовались давно.
FIFO (First In First Out) — удаляем элементы, которые были созданы раньше остальных.
LFU (Least Frequently Used) — чистим записи, которые использовались редко.
*/

// evictionAlgo — интерфейс strategy.
type evictionAlgo interface {
	evict(c *cache)
}

// реализация concreteStrategy

type fifo struct{}

func (l *fifo) evict(c *cache) {
	fmt.Println("Evicting by fifo strategy")
}

type lru struct{}

func (l *lru) evict(c *cache) {
	fmt.Println("Evicting by lru strategy")
}

type lfu struct{}

func (l *lfu) evict(c *cache) {
	fmt.Println("Evicting by lfu strategy")
}

// cache содержит контекст.
type cache struct {
	storage      map[string]string
	evictionAlgo evictionAlgo
	capacity     int
	maxCapacity  int
}

func initCache(e evictionAlgo) *cache {
	storage := make(map[string]string)
	return &cache{
		storage:      storage,
		evictionAlgo: e,
		capacity:     0,
		maxCapacity:  2,
	}
}

// setEvictionAlgo определяет алгоритм освобождения памяти.
func (c *cache) setEvictionAlgo(e evictionAlgo) {
	c.evictionAlgo = e
}

func (c *cache) add(key, value string) {
	if c.capacity == c.maxCapacity {
		c.evict()
	}
	c.capacity++
	c.storage[key] = value
}

func (c *cache) get(key string) {
	delete(c.storage, key)
}

func (c *cache) evict() {
	c.evictionAlgo.evict(c)
	c.capacity--
}

func main() {
	lfu := &lfu{}
	cache := initCache(lfu)
	cache.add("a", "1")
	cache.add("b", "2")
	cache.add("c", "3")

	lru := &lru{}
	cache.setEvictionAlgo(lru)
	cache.add("d", "4")

	fifo := &fifo{}
	cache.setEvictionAlgo(fifo)
	cache.add("e", "5")
}
