package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"os"
)

type Event struct {
	ID       uint    `json:"id"`
	CarModel string  `json:"car_model"`
	Price    float64 `json:"price"`
}

type producer struct {
	file *os.File
	// добавляем writer в Producer
	writer *bufio.Writer
}

func NewProducer(filename string) (*producer, error) {
	file, err := os.OpenFile(filename, os.O_WRONLY|os.O_CREATE|os.O_APPEND, 0777)
	if err != nil {
		return nil, err
	}

	return &producer{
		file: file,
		// создаём новый Writer
		writer: bufio.NewWriter(file),
	}, nil
}

func (p *producer) WriteEvent(event *Event) error {
	data, err := json.Marshal(&event)
	if err != nil {
		return err
	}

	// записываем событие в буфер
	if _, err := p.writer.Write(data); err != nil {
		return err
	}

	// добавляем перенос строки
	if err := p.writer.WriteByte('\n'); err != nil {
		return err
	}

	// записываем буфер в файл
	return p.writer.Flush()
}

type consumer struct {
	file *os.File
	// заменяем reader на scanner
	scanner *bufio.Scanner
}

func NewConsumer(filename string) (*consumer, error) {
	file, err := os.OpenFile(filename, os.O_RDONLY|os.O_CREATE, 0777)
	if err != nil {
		return nil, err
	}

	return &consumer{
		file: file,
		// создаём новый scanner
		scanner: bufio.NewScanner(file),
	}, nil
}

func (c *consumer) ReadEvent() (*Event, error) {
	// одиночное сканирование до следующей строки
	if !c.scanner.Scan() {
		return nil, c.scanner.Err()
	}
	// читаем данные из scanner
	data := c.scanner.Bytes()

	event := Event{}
	err := json.Unmarshal(data, &event)
	if err != nil {
		return nil, err
	}

	return &event, nil
}

func (c *consumer) Close() error {
	return c.file.Close()
}

func main() {
	//defer os.Remove("file.txt")
	prod, _ := NewProducer("file.txt")
	event := Event{
		ID:       12,
		CarModel: "BMW",
		Price:    11.12,
	}
	err := prod.WriteEvent(&event)
	if err != nil {
		log.Fatal(err)
	}

	cons, _ := NewConsumer("file.txt")
	defer cons.Close()
	result, _ := cons.ReadEvent()
	fmt.Printf("%+#v", result) // &main.Event{ID:0xc, CarModel:"BMW", Price:11.12}
}
