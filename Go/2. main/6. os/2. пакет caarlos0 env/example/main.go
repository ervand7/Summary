package main

import (
	"github.com/caarlos0/env/v6"
	"log"
	"time"
)

/*
Предположим, что для конфигурации требуются:
 - список файлов, записанных в переменную FILES и разделённых двоеточием
 - домашняя директория HOME
 - интервал запуска задач TASK_DURATION (если эта переменная отсутствует, завершаем программу с ошибкой)
*/

type Config struct {
	Files        []string      `env:"FILES" envSeparator:":"`
	Home         string        `env:"HOME"`
	TaskDuration time.Duration `env:"TASK_DURATION,required"`
}

func main() {
	var cfg Config
	err := env.Parse(&cfg)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+#v", cfg)
}

// export FILES=test1.txt:test2.txt && export TASK_DURATION=5s
// go run main.go

/*
out:
{[test1.txt test2.txt] /Users/ervand_agadzhanyan 5s}
*/
