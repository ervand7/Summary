package some

import (
	"encoding/xml"
	"runtime"
	"strings"
	"sync"
	"sync/atomic"
	"testing"
	"time"
)

var data string = `
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet title="XSL_formatting" type="text/xsl"?>
<rss>
    <channel>
        <title><![CDATA[BBC News - US & Canada]]></title>
        <description><![CDATA[BBC News - US & Canada]]></description>
        <item>
            <title><![CDATA[President China visit: US leader strik]]></title>
            <description><![CDATA[The US president praises]]></description>
        </item>
    </channel>
</rss>
`

type (
	item struct {
		XMLName     xml.Name `xml:"item"`
		Title       string   `xml:"title"`
		Description string   `xml:"description"`
	}
	channel struct {
		XMLName xml.Name `xml:"channel"`
		Items   []item   `xml:"item"`
	}
	document struct {
		XMLName xml.Name `xml:"rss"`
		Channel channel  `xml:"channel"`
	}
)

func read(doc string) ([]item, error) {
	time.Sleep(time.Millisecond) // Simulate blocking disk read
	var d document
	if err := xml.Unmarshal([]byte(doc), &d); err != nil {
		return nil, err
	}
	return d.Channel.Items, nil
}

func find(topic string, docs []string) int {
	var found int
	for _, doc := range docs {
		items, err := read(doc)
		if err != nil {
			continue
		}
		for _, item := range items {
			if strings.Contains(item.Description, topic) {
				found++
			}
		}
	}
	return found
}

func findConcurrent(goroutines int, topic string, docs []string) int {
	var found int64

	ch := make(chan string, len(docs))
	for _, doc := range docs {
		ch <- doc
	}
	close(ch)

	var wg sync.WaitGroup
	wg.Add(goroutines)

	for g := 0; g < goroutines; g++ {
		go func() {
			var lFound int64
			for doc := range ch {
				items, err := read(doc)
				if err != nil {
					continue
				}
				for _, item := range items {
					if strings.Contains(item.Description, topic) {
						lFound++
					}
				}
			}
			atomic.AddInt64(&found, lFound)
			wg.Done()
		}()
	}

	wg.Wait()

	return int(found)
}

func BenchmarkSequential(b *testing.B) {
	b.StopTimer()
	count := 1000
	docs := make([]string, 0, count)
	for i := 0; i < count; i++ {
		docs = append(docs, data)
	}

	b.StartTimer()
	for i := 0; i < b.N; i++ {
		find("president", docs)
	}
}
func BenchmarkConcurrent(b *testing.B) {
	b.StopTimer()
	count := 1000
	docs := make([]string, 0, count)
	for i := 0; i < count; i++ {
		docs = append(docs, data)
	}

	b.StartTimer()
	for i := 0; i < b.N; i++ {
		findConcurrent(runtime.NumCPU(), "president", docs)
	}
}
