package main

import (
	"net/http"
	"testing"
)

func TestDownload(t *testing.T) {
	tt := []struct {
		name       string
		url        string
		statusCode int
	}{
		{
			"ok",
			"https://www.ardanlabs.com/blog/index.xml",
			http.StatusOK,
		},
		{
			"notfound",
			"http://rss.cnn.com/rss/cnn_topstorie.rss",
			http.StatusNotFound,
		},
	}
	for _, test := range tt {
		test := test // <- LOOK HERE
		tf := func(t *testing.T) {
			t.Parallel() // <- LOOK HERE
			resp, err := http.Get(test.url)
			if err != nil {
				t.Fatalf("unable to issue GET/URL: %s: %s", test.url, err)
			}
			defer resp.Body.Close()

			if resp.StatusCode != test.statusCode {
				t.Log("exp:", test.statusCode)
				t.Log("got:", resp.StatusCode)
				t.Fatal("status codes don’t match")
			}
		}

		t.Run(test.name, tf) // <- LOOK HERE
	}
}
