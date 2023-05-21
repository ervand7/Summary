package hashbyte

import "io"

type Hasher interface {
	// Writer мы встроили интерфейс io.Writer в наш интерфейс,
	// чтобы задать требование по наличию метода Write
	io.Writer
	Hash() byte
}

type hash struct {
	result byte
}

func New(val byte) Hasher {
	return &hash{
		result: val,
	}
}

func (h *hash) Write(bytes []byte) (n int, err error) {
	for _, b := range bytes {
		h.result = (h.result^b)<<1 + b%2
	}
	return len(bytes), nil
}

func (h hash) Hash() byte {
	return h.result
}
