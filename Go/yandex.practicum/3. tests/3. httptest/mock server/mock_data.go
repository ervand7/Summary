package some

import (
	"fmt"
	"log"
	"net/http"
	"net/http/httptest"
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

// Create a mock server by any params we need
func mockServer() *httptest.Server {
	f := func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(200)
		w.Header().Set("Content-Type", "application/xml")

		if _, err := fmt.Fprintln(w, feed); err != nil {
			log.Fatal(err.Error())
		}

	}
	return httptest.NewServer(http.HandlerFunc(f))
}
