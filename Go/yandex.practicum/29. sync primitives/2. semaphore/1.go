package main

import (
	"context"
	"errors"

	"golang.org/x/sync/semaphore"
)

type VideoEncoder interface {
	SubmitEncodingTask(ctx context.Context, file VideoFile) (chan EncodingResult, error)
}

type EncodingResult struct {
	// one of — в каждый момент времени только одно из полей этой структуры не равно nil

	OK  *EncodingResultOK
	Err error
}

type EncodingResultOK struct {
	URL string
}

type VideoFile struct {
	URL          string // местонахождение файла
	DurationMins int64
}

type videoEncoder struct {
	sem *semaphore.Weighted
}

// NewVideoEncoder конструктор конвертера с пропускной способностью n
func NewVideoEncoder(n int64) videoEncoder {
	var ve videoEncoder
	// конструируем семафор с общей ёмкостью n
	ve.sem = semaphore.NewWeighted(n)
	return ve
}

var _ VideoEncoder = (*videoEncoder)(nil)

func (e *videoEncoder) SubmitEncodingTask(
	ctx context.Context, file VideoFile,
) (chan EncodingResult, error) {
	// пробуем поставить в очередь задачу на конвертацию видео
	// длина видео — file.DurationMins минут
	if ok := e.sem.TryAcquire(file.DurationMins); !ok {
		// если не получилось — попробуем в другой раз
		return nil, errors.New("too many videos in queue")
	}

	return e.doEncode(ctx, file)
}

func (e *videoEncoder) doEncode(
	ctx context.Context, file VideoFile,
) (chan EncodingResult, error) {
	resultChan := make(chan EncodingResult)
	go func(ctx context.Context, file VideoFile) {
		// уменьшаем очередь на file.DurationMins
		defer e.sem.Release(file.DurationMins)

		// тут делаем реальную декодировку видео
	}(ctx, file)

	return resultChan, nil
}
