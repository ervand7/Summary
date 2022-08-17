package main

// Person содержит информацию о пользователе и описывает сериализацию в JSON и YAML.
type Person struct {
	ID    int
	Name  string `yaml:"name"`
	Email string `json:"email" yaml:"email"`
}
