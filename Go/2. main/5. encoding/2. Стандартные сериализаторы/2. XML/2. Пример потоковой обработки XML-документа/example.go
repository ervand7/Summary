package main

import (
	"bytes"
	"encoding/xml"
	"errors"
	"fmt"
	"io"
)

const MockXMLDocument = `
<?xml version="1.0" encoding="UTF-8"?>
<storage-report version="1.0" exported-on="2021-01-31" location-id="001">
<item barcode="000000000001">
  <quantity>100</quantity>
</item>
<item barcode="000000000002">
  <quantity>500</quantity>
</item>
</storage-report>
`

// Item — XML-представление складской единицы.
type Item struct {
	XMLName  xml.Name `xml:"item"`
	Barcode  string   `xml:"barcode,attr"`
	Quantity int64    `xml:"quantity"`
}

// ProcessStorageReportStream обрабатывает XML-отчёт по складу.
func ProcessStorageReportStream(stream io.Reader) error {
	decoder := xml.NewDecoder(stream)
	for {
		// получаем следующий XML-токен
		xmlToken, err := decoder.Token()
		if err != nil {
			// проверка на конец файла
			if errors.Is(err, io.EOF) {
				break
			}
			// ошибка чтения
			return fmt.Errorf("reading XML token: %w", err)
		}

		switch xmlElement := xmlToken.(type) {
		case xml.StartElement:
			// идентифицируем XML-элемент по имени
			if xmlElement.Name.Local == "item" {
				var item Item
				if err := decoder.DecodeElement(&item, &xmlElement); err != nil {
					return fmt.Errorf("XML decode to (%T): %w", item, err)
				}
				HandleReportItem(item)
			}
		default:
		}
	}

	return nil
}

// HandleReportItem обрабатывает складскую единицу из отчёта.
func HandleReportItem(item Item) {
	fmt.Printf("Обработка складской позиции (%s):\n", item.Barcode)
	fmt.Printf("  Количество [шт]: %d\n", item.Quantity)
}

func main() {
	reader := bytes.NewReader([]byte(MockXMLDocument))
	if err := ProcessStorageReportStream(reader); err != nil {
		panic(err)
	}
}
