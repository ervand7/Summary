package main

import (
	"encoding/csv"
	"encoding/json"
	"io"
	"log"
	"net/http"
	"strconv"
	"strings"
)

type summary struct {
	Column string  `json:"column"`
	Sum    float64 `json:"sum"`
}

func summarizeCSV(data []byte) ([]summary, error) {
	reader := csv.NewReader(strings.NewReader(string(data)))

	header, err := reader.Read()
	if err != nil {
		return nil, err
	}

	sums := make([]float64, len(header))

	for {
		rec, err := reader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			continue
		}

		for i, v := range rec {
			f, _ := strconv.ParseFloat(v, 64)
			sums[i] += f
		}
	}

	out := make([]summary, len(header))
	for i, col := range header {
		out[i] = summary{
			Column: col,
			Sum:    sums[i],
		}
	}

	return out, nil
}

func summarizeHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}

	data, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "cannot read body", http.StatusBadRequest)
		return
	}

	list, err := summarizeCSV(data)
	if err != nil {
		http.Error(w, "csv error", http.StatusBadRequest)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	_ = json.NewEncoder(w).Encode(list)
}

func main() {
	http.HandleFunc("/summarize", summarizeHandler)
	log.Println("CSV Summarizer listening on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
