package main

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
)

// The first thing the test does is use the init function to make sure all the
// routes are loaded in the mux. This is done by calling the handlers.Routes
// function. A big mistake that is made with these types of tests is
// forgetting to load the routes.
func init() {
	Routes()
}

func Routes() {
	http.HandleFunc("/sendjson", sendJSON)
}

func sendJSON(rw http.ResponseWriter, r *http.Request) {
	u := struct {
		Name  string
		Email string
	}{
		Name:  "Bill",
		Email: "bill@ardanlabs.com",
	}
	rw.Header().Set("Content-Type", "application/json")
	rw.WriteHeader(200)
	json.NewEncoder(rw).Encode(&u)
}

func TestSendJSON(t *testing.T) {
	url := "/sendjson"
	statusCode := 200
	r := httptest.NewRequest("GET", url, nil)
	w := httptest.NewRecorder()
	http.DefaultServeMux.ServeHTTP(w, r)

	if w.Code != 200 {
		t.Log("exp:", statusCode)
		t.Log("got:", w.Code)
		t.Fatal("status codes don’t match")
	}

	var u struct {
		Name  string
		Email string
	}
	if err := json.NewDecoder(w.Body).Decode(&u); err != nil {
		t.Fatal("unable to decode the response:", err)
	}

	expectedName := "Bill"
	if u.Name != expectedName {
		t.Log("exp:", expectedName)
		t.Log("got:", u.Name)
		t.Fatal("user name does not match")
	}

	expectedEmail := "bill@ardanlabs.com"
	if u.Email != expectedEmail {
		t.Log("exp:", expectedEmail)
		t.Log("got:", u.Email)
		t.Fatal("user name does not match")
	}
}
