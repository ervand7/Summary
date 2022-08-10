package main

import (
	"encoding/json"
	"fmt"
)

/*
Есть пример API-вызова в формате JSON:
{
    "header": {
        "code": 0,
        "message": ""
    },
    "data": [{
        "type": "user",
        "id": 100,
        "attributes": {
            "email": "bob@yandex.ru",
            "article_ids": [10, 11, 12]
        }
    }]
}
К сожалению, ни Swagger-описания, ни статьи с API-ответом в любимом
сервисе заметок — нет. Опишите данный объект в виде структуры на Go,
в учебных целях отбросив «так делать нельзя» и «это не дело».
На входе есть строка с сырыми данными, требуется написать функцию её десериализации
*/

type Header struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
}
type inData struct {
	Type       string     `json:"type"`
	Id         int        `json:"id"`
	Attributes Attributes `json:"attributes"`
}
type Attributes struct {
	Email      string `json:"email"`
	ArticleIds []int  `json:"article_ids"`
}
type Response_ struct {
	Header Header   `json:"header"`
	Data   []inData `json:"data"`
}

func main() {
	jsonString := `{
    "header": {
        "code": 0,
        "message": ""
    },
    "data": [{
        "type": "user",
        "id": 100,
        "attributes": {
            "email": "bob@yandex.ru",
            "article_ids": [10, 11, 12]
        }
    }]
}`
	var response Response_
	err := json.Unmarshal([]byte(jsonString), &response)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("%+v\n", response)
}

// {Header:{Code:0 Message:} Data:[{Type:user Id:100 Attributes:{Email:bob@yandex.ru ArticleIds:[10 11 12]}}]}
