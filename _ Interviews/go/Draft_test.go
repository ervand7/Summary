package main

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"testing"
)

var feed = `<?xml version="1.0" encoding="UTF-8"?>
<rss>
<channel>
 <title>Going Go Programming</title>
 <description>Golang : https://github.com/goinggo</description>
 <link>http://www.goinggo.net/</link>
 <item>
 <pubDate>Sun, 15 Mar 2015 15:04:00 +0000</pubDate>
 <title>Object Oriented Programming Mechanics</title>
 <description>Go is an object oriented language.</description>
 <link>http://www.goinggo.net/2015/03/object-oriented</link>
 </item>
</channel>
</rss>`

func mockServer() *httptest.Server {
	f := func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)
		w.Header().Set("Content-Type", "application/xml")
		fmt.Fprintln(w, feed)
	}
	return httptest.NewServer(http.HandlerFunc(f))
}

func TestDownload(t *testing.T) {
	statusCode := 200
	server := mockServer()
	defer server.Close()

	resp, err := http.Get(server.URL)
	if err != nil {
		t.Fatalf("unable to issue GET on the URL: %s: %s", server.URL, err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != statusCode {
		t.Log("exp:", statusCode)
		t.Log("got:", resp.StatusCode)
		t.Fatal("status codes don’t match")
	}
}
