package UserExists

import "fmt"

type DBStorage interface {
	UserExists(email string) bool
}

// NewUser обратите внимание, что DBStorage передаётся в
// функцию в качестве параметра, таким образом мы можем при
// тестировании подменить реальную БД тестовой заглушкой.
func NewUser(db DBStorage, email string) error {
	if db.UserExists(email) {
		return fmt.Errorf(`user with '%s' email already exists`, email)
	}
	// добавляем запись
	return nil
}
