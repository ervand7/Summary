package main

import (
	"go.uber.org/zap"
	"log"
	"os"
)

func main() {
	logger, err := New("info")
	if err != nil {
		log.Fatal(err)
	}

	logger.Debug("check debug")
	logger.Info("check info")
	logger.Warn("check warn")
	logger.Error("check error")
	//logger.Fatal("check fatal")

	/*
		{"level":"info","ts":1661889205.139833,"caller":"main/main.go:12","msg":"check info"}
		{"level":"warn","ts":1661889205.139921,"caller":"main/main.go:13","msg":"check warn"}
		{"level":"error","ts":1661889205.1399271,"caller":"main/main.go:14","msg":"check error","stacktrace":"main.main\n\t/Users/ervand_agadzhanyan/Desktop/Summary/Go/yandex.practicum/0. logging/zap/main/main.go:14\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:250"}
		{"level":"fatal","ts":1661889205.1399481,"caller":"main/main.go:15","msg":"check fatal","stacktrace":"main.main\n\t/Users/ervand_agadzhanyan/Desktop/Summary/Go/yandex.practicum/0. logging/zap/main/main.go:15\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:250"}
	*/

	_, fileReadErr := os.ReadFile("hello.txt")
	if fileReadErr != nil {
		logger.Fatal("file does not exists", zap.Error(fileReadErr))
	}
	/*
		{
			"level":"fatal",
			"ts":1661889527.389531,
			"caller":"main/main.go:30",
			"msg":"file does not exists",
			"error":"open hello.txt: no such file or directory","stacktrace":"main.main\n\t/Users/ervand_agadzhanyan/Desktop/Summary/Go/yandex.practicum/0. logging/zap/main/main.go:30\nruntime.main\n\t/usr/local/go/src/runtime/proc.go:250"
		}
	*/
}
