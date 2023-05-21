package some

import (
	"encoding/xml"
	"net/http"
	"testing"
)

// Document defines the fields associated with the buoy RSS document.
type Document struct {
	XMLName xml.Name `xml:"rss"`
	Channel Channel  `xml:"channel"`
	URI     string
}

type Item struct {
	XMLName     xml.Name `xml:"item"`
	Title       string   `xml:"title"`
	Description string   `xml:"description"`
	Link        string   `xml:"link"`
}

// Channel defines the fields associated with the channel tag in the buoy RSS document
type Channel struct {
	XMLName     xml.Name `xml:"channel"`
	Title       string   `xml:"title"`
	Description string   `xml:"description"`
	Link        string   `xml:"link"`
	PubDate     string   `xml:"pubDate"`
	Items       []Item   `xml:"item"`
}

func TestDownload_(t *testing.T) {
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

	var d Document
	if err = xml.NewDecoder(resp.Body).Decode(&d); err != nil {
		t.Fatal("unable to decode the response:", err)
	}
	if len(d.Channel.Items) != 1 {
		t.Fatal("not seeing 1 item in the feed: len:",
			len(d.Channel.Items))
	}
}
