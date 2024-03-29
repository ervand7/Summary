package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

/*
Бывают ситуации, когда нужно выполнить определённые действия только один раз.
Для этого достаточно определить переменную типа sync.Once и вызвать для
неё метод Do, который в параметре принимает функцию. От этой принимаемой функции мы
ожидаем, что она отработает только один раз.

В качестве примера напишем код, который вычитывает конфиг (Config) и
инициализирует структуру.
*/

type Config struct {
	once sync.Once
	vals map[string]string
}

func (c *Config) Get(k string) (string, bool) {
	c.once.Do(func() { // эта функция отработает только 1 раз
		fmt.Print("Hello\n") // для дебага, чтобы было видно, что функция отрабатывает 1 раз
		c.vals = map[string]string{
			"host": "127.0.0.1",
			"port": fmt.Sprintf("%d", rand.Intn(65535)),
		}
	})

	v, ok := c.vals[k]
	return v, ok
}

func main() {
	var cfg Config

	keys := []string{"host", "port", "port", "host", "port"}
	for _, k := range keys {
		go func(k string) {
			// в одной из горутин произойдёт инициализация cfg
			// остальные горутины будут ждать завершения инициализации
			v, ok := cfg.Get(k)
			if !ok {
				return
			}
			fmt.Printf("%s = %s\n", k, v)
		}(k)
	}

	time.Sleep(1 * time.Second)
}

/*
Hello
host = 127.0.0.1
port = 53126
port = 53126
host = 127.0.0.1
port = 53126

А если бы не было sync.Once, результат был бы что-то типа:
Hello
host = 127.0.0.1
Hello
host = 127.0.0.1
Hello
port = 41687
Hello
port = 15554
Hello
port = 48091
*/

