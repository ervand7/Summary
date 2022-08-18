package main

import (
	"encoding/xml"
	"time"
)

type (
	RaceReport struct {
		XMLName             xml.Name      `xml:"report"`
		CompetitionDate     time.Time     `xml:"competition>date"`
		CompetitionLocation string        `xml:"competition>location"`
		CompetitionClass    string        `xml:"competition>class"`
		Results             []RacerResult `xml:"racer"`
	}

	RacerResult struct {
		XMLName   xml.Name `xml:"racer"`
		GlobalId  int      `xml:"global_id,attr,omitempty"`
		Nick      string   `xml:"nick"`
		BestLapMs int64    `xml:"best_lap_ms"`
		Laps      float32  `xml:"laps"`
		Comment   string   `xml:",comment"`
	}
)
