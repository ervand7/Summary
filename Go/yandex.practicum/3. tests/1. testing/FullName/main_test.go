package FullName

import "testing"

func TestUser_FullName(t *testing.T) {
	type fields struct {
		FirstName string
		LastName  string
	}
	tests := []struct {
		name   string
		fields fields
		want   string
	}{
		{
			name:   "short values",
			fields: fields{FirstName: "a", LastName: "b"},
			want:   "a b",
		},
		{
			name:   "long values",
			fields: fields{FirstName: "qwertyuiopasdfg", LastName: "zxcvbnmlkjhgfd"},
			want:   "qwertyuiopasdfg zxcvbnmlkjhgfd",
		},
		{
			name:   "nums in values",
			fields: fields{FirstName: "1qwerty2uiopasdfg", LastName: "z3xcvbnm4lkjhgfd"},
			want:   "1qwerty2uiopasdfg z3xcvbnm4lkjhgfd",
		},
		{
			name:   "diff registers",
			fields: fields{FirstName: "qweASD", LastName: "XCVer"},
			want:   "qweASD XCVer",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			u := User{
				FirstName: tt.fields.FirstName,
				LastName:  tt.fields.LastName,
			}
			if got := u.FullName(); got != tt.want {
				t.Errorf("FullName() = %v, want %v", got, tt.want)
			}
		})
	}
}
