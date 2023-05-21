package some

import (
	"net/http"
	"testing"
)

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
