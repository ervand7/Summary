package json

import (
	"encoding/json"
	"testing"

	jsoniter "github.com/json-iterator/go"
)

type Student struct {
	Name       string   `json:"name"`
	Phone      string   `json:"phone"`
	Age        uint     `json:"age"`
	Rate       uint     `json:"rate"`
	CourseList []string `json:"course_list"`
}

var rawJSON = []byte(`{"name":"Foo Bar","phone":"+31920334010","age":30,"rate":250,"course_list":["medieval literature","history","design","art","choreography"]}`)

func BenchmarkStdMarshal(b *testing.B) {
	s := &Student{}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_, _ = json.Marshal(s)
	}
}

func BenchmarkStdUnmarshal(b *testing.B) {
	s := &Student{}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_ = json.Unmarshal(rawJSON, s)
	}
}

func BenchmarkJsoniterMarshal(b *testing.B) {
	s := &Student{}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_, _ = jsoniter.Marshal(s)
	}
}

func BenchmarkJsoniterUnmarshal(b *testing.B) {
	s := &Student{}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		_ = jsoniter.Unmarshal(rawJSON, s)
	}
}
