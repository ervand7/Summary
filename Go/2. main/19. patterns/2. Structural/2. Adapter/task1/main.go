package task1

/*
Есть интерфейсы JSONData и YAMLData с функцией декодирования.
Объект типа Client получает данные в JSON-формате и декодирует их.
Возникла ситуация, когда данные приходят с объектом, который
поддерживает интерфейс YAMLData. Реализуйте Адаптер для успешной работы
клиента с данными в формате YAML.
*/

// JSONData — интерфейс для декодирования JSON.
type JSONData interface {
	DecodeJSON() interface{}
}

// YAMLData — интерфейс для декодирования YAML.
type YAMLData interface {
	DecodeYAML() interface{}
}

type Client struct {
	Data interface{}
}

func (client *Client) Decode(input JSONData) {
	client.Data = input.DecodeJSON()
}

type Adapter struct {
	data YAMLData
}

func (a *Adapter) DecodeYAML() interface{} {
	return 5
}

func (a *Adapter) DecodeJSON() interface{} {
	return a.data.DecodeYAML()
}

func Load(client Client, input YAMLData) {
	adapter := &Adapter{
		data: input,
	}
	client.Decode(adapter)
}
