package main

type Reader interface {
	Read(p []byte) (n int, err error)
}

type Writer interface {
	Write(p []byte) (n int, err error)
}

// FileHandle В итоге интерфейс FileHandle будет содержать три метода: Read, Write и Close.
type FileHandle interface {
	Reader
	Writer
	Close() error
}
