package example

import "github.com/google/uuid"

// User демонстрирует пример описания GORM-модели.
type User struct {
	ID    uuid.UUID `gorm:"type:uuid;default:uuid_generate_v4()"`
	Name  string    `gorm:"size:255"` // указывает размер поля
	Email string    `gorm:"type:varchar (100);unique_index"`
	Phone string    `gorm:"index:phone"` // создаёт индекс для этого поля
	mark  int       `gorm:"-"`           // не участвует в модели
}
