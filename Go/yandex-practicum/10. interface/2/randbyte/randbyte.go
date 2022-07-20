package randbyte

import (
	"encoding/binary"
	"io"
	"math/rand"
)

type generator struct {
	rnd rand.Source
}

func New(seed int64) io.Reader {
	return &generator{
		rnd: rand.NewSource(seed),
	}
}

// First variant:
//func (g *generator) Read(bytes []byte) (n int, err error) {
//	for i := range bytes {
//		randInt := g.rnd.Int63()
//		randByte := byte(randInt)
//		bytes[i] = randByte
//	}
//	return len(bytes), nil
//}

// Second variant
func (g *generator) Read(bytes []byte) (n int, err error) {
	for i := 0; i+8 < len(bytes); i += 8 {
		randValue := g.rnd.Int63()
		randValue64 := uint64(randValue)
		bytesPrepared := bytes[i : i+8]
		binary.LittleEndian.PutUint64(bytesPrepared, randValue64)
	}
	return len(bytes), nil
}
