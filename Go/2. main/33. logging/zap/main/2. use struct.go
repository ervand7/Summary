package main

import (
	"go.uber.org/zap"
	"time"
)

type Event struct {
	Id   int
	Type string
	Time time.Time
}

func some() {
	event := Event{1, "CreateEvent", time.Now()}

	// выводим по полям
	logger, _ := New("info")
	logger.Info(
		"create event",
		zap.Int("EventId", event.Id),
		zap.String("EventType", event.Type),
		zap.Time("EventTime", event.Time),
	)
}

/*
{
	"level":"info",
	"ts":1661890264.455505,
	"caller":"main/2. use struct.go:19",
	"msg":"create event",
	"EventId":1,
	"EventType":"CreateEvent",
	"EventTime":1661890264.455481
}
*/
