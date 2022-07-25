package UserExists

import (
	"fmt"
	"github.com/stretchr/testify/require"
	"testing"
)

// DBMock тип объекта-заглушки
type DBMock struct {
	emails map[string]bool
}

// UserExists для удовлетворения интерфейсу DBStorage реализуем
func (db *DBMock) UserExists(email string) bool {
	return db.emails[email]
}

// addUser вспомогательный метод, для подсовывания тестовых данных
func (db *DBMock) addUser(email string) {
	db.emails[email] = true
}

func TestNewUser(t *testing.T) {
	errPattern := `user with '%s' email already exists`
	tbl := []struct {
		name    string
		email   string
		preset  bool
		wanterr bool
	}{
		{`want success`, `gregorysmith@myexampledomain.com`, false, false},
		{`want error`, `johndoe@myexampledomain.com`, true, true},
	}
	for _, item := range tbl {
		t.Run(item.name, func(t *testing.T) {
			// создаём объект-заглушку
			dbMock := &DBMock{emails: make(map[string]bool)}
			if item.preset {
				dbMock.addUser(item.email)
			}
			// выполняем наш код, передавая объект-заглушку
			err := NewUser(dbMock, item.email)
			if !item.wanterr {
				require.NoError(t, err)
			} else {
				require.EqualError(t, err, fmt.Sprintf(errPattern, item.email))
			}
		})
	}
}
