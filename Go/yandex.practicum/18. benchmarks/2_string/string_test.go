package __string

import (
	"regexp"
	"strings"
	"testing"
)

const (
	s   = "We cannot apply a single standard, benchmark or template to all regions."
	sub = "standard"
)

func rgx(s, substr string) bool {
	res, _ := regexp.MatchString(substr, s)
	return res
}

func std(s, substr string) bool {
	return strings.Contains(s, substr)
}

func Test_Substr(t *testing.T) {
	t.Run("regexp", func(t *testing.T) {
		if !rgx(s, sub) {
			t.Errorf("rgx failed")
		}
	})
	t.Run("std", func(t *testing.T) {
		if !std(s, sub) {
			t.Errorf("std failed")
		}
	})
}

func BenchmarkStd(b *testing.B) {
	for i := 0; i < b.N; i++ {
		std(s, sub)
	}
}

func BenchmarkRgx(b *testing.B) {
	for i := 0; i < b.N; i++ {
		rgx(s, sub)
	}
}
