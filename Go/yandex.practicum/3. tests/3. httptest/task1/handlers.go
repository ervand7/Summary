package task1

import (
	"encoding/json"
	"net/http"
)

// User — основной объект для теста.
type User struct {
	ID        string
	FirstName string
	LastName  string
}

// UserViewHandler — хендлер, который нужно протестировать.
func UserViewHandler(users map[string]User) http.HandlerFunc {
	return func(rw http.ResponseWriter, r *http.Request) {
		userId := r.URL.Query().Get("user_id")
		if r.URL.Query().Get("user_id") == "" {
			http.Error(rw, "user_id is empty", http.StatusBadRequest)
			return
		}

		user, ok := users[userId]
		if !ok {
			http.Error(rw, "user not found", http.StatusNotFound)
			return
		}

		jsonUser, err := json.Marshal(user)
		if err != nil {
			http.Error(rw, "can't provide a json. internal error", http.StatusInternalServerError)
			return
		}

		rw.WriteHeader(http.StatusOK)
		rw.Write(jsonUser)
	}
}
