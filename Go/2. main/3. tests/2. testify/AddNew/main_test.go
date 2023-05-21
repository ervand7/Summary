package AddNew

import (
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"testing"
)

func TestFamily_AddNew(t *testing.T) {
	type newPerson struct {
		r Relationship
		p Person
	}
	tests := []struct {
		name      string
		family    map[Relationship]Person
		newPerson newPerson
		wantErr   bool
	}{
		{
			name: "add father",
			family: map[Relationship]Person{
				Mother: {
					FirstName: "Maria",
					LastName:  "Popova",
					Age:       36,
				},
			},
			newPerson: newPerson{
				r: Father,
				p: Person{
					FirstName: "Misha",
					LastName:  "Popov",
					Age:       42,
				},
			},
			wantErr: false,
		},
		{
			name: "error Father already exists",
			family: map[Relationship]Person{
				Father: {
					FirstName: "Misha",
					LastName:  "Popov",
					Age:       42,
				},
			},
			newPerson: newPerson{
				r: Father,
				p: Person{
					FirstName: "Ken",
					LastName:  "Gymsohn",
					Age:       32,
				},
			},
			wantErr: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			f := &Family{
				Members: tt.family,
			}
			err := f.AddNew(tt.newPerson.r, tt.newPerson.p)
			if !tt.wantErr {
				// обязательно проверяем на ошибки
				require.NoError(t, err)
				// дополнительно проверяем, что новый человек был добавлен
				assert.Contains(t, f.Members, tt.newPerson.r)
				return
			}

			assert.Error(t, err)
		})
	}
}
