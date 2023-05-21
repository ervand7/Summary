package main

import (
	"encoding/json"
	"fmt"
	"reflect"
	"strconv"
	"strings"
)

type (
	// FieldsInfo содержит информацию о полях структуры (ключ: имя поля).
	FieldsInfo map[string]FieldInfo

	// FieldInfo содержит информацию о поле структуры.
	FieldInfo struct {
		// тип поля
		Type string `json:"type"`
		// теги
		Tags TagsInfo `json:"tags,omitempty"`
		// информация по полям вложенной структуры
		Embedded FieldsInfo `json:"embedded,omitempty"`
	}

	// TagsInfo содержит информацию о тегах (ключ: имя тега).
	TagsInfo map[string][]string
)

// String возвращает строковую репрезентацию типа FieldsInfo.
func (f FieldsInfo) String() string {
	bz, _ := json.MarshalIndent(f, "", "   ")
	return string(bz)
}

// GetStructTags возвращает информацию по каждому полю структуры.
func GetStructTags(obj interface{}) (retInfos FieldsInfo) {
	retInfos = make(FieldsInfo)

	// получаем описание типа переданного объекта
	// далее по коду явно передаём в функцию тип `reflect.Type`, поддержим здесь этот случай рекурсивного вызова
	var objType reflect.Type
	if t, ok := obj.(reflect.Type); ok {
		objType = t
	} else {
		objType = reflect.ValueOf(obj).Type()
	}

	// чиним вход: если передали указатель, получим описание типа под указателем
	if objType.Kind() == reflect.Ptr {
		objType = objType.Elem()
	}

	// проверка входа: если объект не структура, искать теги не нужно
	if objType.Kind() != reflect.Struct {
		return
	}

	// итерируемся по всем полям структуры
	// NumField() — возвращает количество полей в структуре
	for fieldIdx := 0; fieldIdx < objType.NumField(); fieldIdx++ {
		field := objType.Field(fieldIdx) // получаем поле структуры
		retInfos[field.Name] = FieldInfo{
			Type:     field.Type.String(),               // тип структуры
			Tags:     parseTagString(string(field.Tag)), // теги структуры
			Embedded: GetStructTags(field.Type),         // рекурсивно вызываем для каждого поля эту же функцию; если поле структура, то пройдемся и по ней.
		}
	}

	return
}

// parseTagString десериализует тег-строку поля структуры.
// Дедупликация имён тегов: первый по порядку (слева направо).
// Ограничения: значение тега не может содержать символы ':' и '"'.
func parseTagString(tagRaw string) (retInfos TagsInfo) {
	retInfos = make(TagsInfo)

	// пример строки: json:"name" pg:"nullable,sortable"
	for _, tag := range strings.Split(tagRaw, " ") {
		if tag = strings.TrimSpace(tag); tag == "" {
			continue
		}

		tagParts := strings.Split(tag, ":")
		if len(tagParts) != 2 {
			continue
		}

		tagName := strings.TrimSpace(tagParts[0])
		if _, found := retInfos[tagName]; found {
			continue
		}

		tagValuesRaw, _ := strconv.Unquote(tagParts[1])
		tagValues := make([]string, 0)
		for _, value := range strings.Split(tagValuesRaw, ",") {
			if value = strings.TrimSpace(value); value != "" {
				tagValues = append(tagValues, value)
			}
		}

		retInfos[tagName] = tagValues
	}

	return
}

type (
	TestStruct struct {
		Id        string `json:"id" format:"uuid" example:"68b69bd2-8db6-4b7f-b7f0-7c78739046c6"`
		Name      string `json:"name" example:"Bob"`
		Group     Group  `json:"group"`
		CreatedAt int64  `json:"created_at" format:"unix" example:"1622647813"`
	}

	Group struct {
		Id             uint64   `json:"id"`
		PermsOverrides []string `json:"overrides" example:"USERS_RW,COMPANY_RWC"`
	}
)

func main() {
	var s *TestStruct
	fmt.Println(GetStructTags(s))
}

/*
{
   "CreatedAt": {
      "type": "int64",
      "tags": {
         "example": [
            "1622647813"
         ],
         "format": [
            "unix"
         ],
         "json": [
            "created_at"
         ]
      }
   },
   "Group": {
      "type": "main.Group",
      "tags": {
         "json": [
            "group"
         ]
      },
      "embedded": {
         "Id": {
            "type": "uint64",
            "tags": {
               "json": [
                  "id"
               ]
            }
         },
         "PermsOverrides": {
            "type": "[]string",
            "tags": {
               "example": [
                  "USERS_RW",
                  "COMPANY_RWC"
               ],
               "json": [
                  "overrides"
               ]
            }
         }
      }
   },
   "Id": {
      "type": "string",
      "tags": {
         "example": [
            "68b69bd2-8db6-4b7f-b7f0-7c78739046c6"
         ],
         "format": [
            "uuid"
         ],
         "json": [
            "id"
         ]
      }
   },
   "Name": {
      "type": "string",
      "tags": {
         "example": [
            "Bob"
         ],
         "json": [
            "name"
         ]
      }
   }
}
*/
