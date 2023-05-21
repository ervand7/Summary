package ApiClient

import (
	"errors"
	"testing"
)

func TestMock(t *testing.T) {
	tbl := []struct {
		query string
		resp  Response
		err   error
	}{
		{"success", Response{"Success", 200}, nil},
		{"error", Response{"", 500}, errors.New("something is wrong")},
		{"empty", Response{"", 404}, nil},
	}
	for _, item := range tbl {
		m := &Mock{}
		m.SetResponse(item.resp, item.err)
		resp, err := m.GetData(item.query)
		if resp.Text != item.resp.Text {
			t.Errorf(`%s: want %v got %v`, item.query, item.resp.Text, resp.Text)
		}
		if !errors.Is(err, item.err) {
			t.Errorf(`%s: want %v got %v`, item.query, item.err, err)
		}
	}
}
