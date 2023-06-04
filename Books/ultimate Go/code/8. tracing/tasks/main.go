package main

import (
	"context"
	"encoding/xml"
	"fmt"
	"io"
	"log"
	"os"
	"runtime"
	"runtime/debug"
	"runtime/trace"
	"strings"
	"sync"
	"sync/atomic"
)

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

func main() {
	debug.SetGCPercent(1000)
	trace.Start(os.Stdout)
	defer trace.Stop()

	docs := make([]string, 4000)
	for i := range docs {
		docs[i] = fmt.Sprintf("newsfeed-%.4d.xml", i)
	}
	topic := "president"
	n := freq(topic, docs)
	log.Printf("Search %d files, found %s %d times.", len(docs), topic, n)
}

func freq(topic string, docs []string) int {
	var found int32
	g := runtime.GOMAXPROCS(0)
	var wg sync.WaitGroup
	wg.Add(g)
	ch := make(chan string, g)

	for i := 0; i < g; i++ {
		go func() {
			var lFound int32
			defer func() {
				atomic.AddInt32(&found, lFound)
				wg.Done()
			}()

			for doc := range ch {
				ctx, task := trace.NewTask(context.Background(), doc)
				reg := trace.StartRegion(ctx, "OpenFile")

				file := fmt.Sprintf("%s.xml", doc[:8])
				f, err := os.OpenFile(file, os.O_RDONLY, 0)
				if err != nil {
					log.Printf("Opening Document [%s] : ERROR : %v", doc, err)
					found = 0
					return
				}
				reg.End()
				reg = trace.StartRegion(ctx, "ReadAll")

				data, err := io.ReadAll(f)
				if err != nil {
					log.Printf("Reading Document [%s] : ERROR : %v", doc, err)
					found = 0
					return
				}
				reg.End()
				f.Close()

				reg = trace.StartRegion(ctx, "Unmarshal")
				var d document
				if err := xml.Unmarshal(data, &d); err != nil {
					log.Printf("Decoding Document [%s] : ERROR : %v", doc, err)
					found = 0
					return
				}
				reg.End()

				reg = trace.StartRegion(ctx, "Contains")
				for _, item := range d.Channel.Items {
					if strings.Contains(item.Title, topic) {
						lFound++
						continue
					}
					if strings.Contains(item.Description, topic) {
						lFound++
					}
				}
				reg.End()
				task.End()
			}
		}()

	}

	for _, doc := range docs {
		ch <- doc
	}
	close(ch)
	wg.Wait()
	return int(found)
}
