package main

import "fmt"

// CircularBuffer реализует структуру данных «кольцевой буфер» для значений float64.
type CircularBuffer struct {
	values  []float64 // текущие значения буфера
	headIdx int       // индекс головы (первый непустой элемент)
	tailIdx int       // индекс хвоста (первый пустой элемент)
}

// GetCurrentSize возвращает текущую длину буфера.
func (b CircularBuffer) GetCurrentSize() int {
	if b.tailIdx < b.headIdx {
		return b.tailIdx + cap(b.values) - b.headIdx
	}

	return b.tailIdx - b.headIdx
}

// GetValues возвращает слайс текущих значений буфера, сохраняя порядок записи.
func (b CircularBuffer) GetValues() (retValues []float64) {
	for i := b.headIdx; i != b.tailIdx; i = (i + 1) % cap(b.values) {
		retValues = append(retValues, b.values[i])
	}

	return
}

// AddValue добавляет новое значение в буфер.
func (b *CircularBuffer) AddValue(v float64) {
	b.values[b.tailIdx] = v
	b.tailIdx = (b.tailIdx + 1) % cap(b.values)
	if b.tailIdx == b.headIdx {
		b.headIdx = (b.headIdx + 1) % cap(b.values)
	}
}

// NewCircularBuffer — конструктор типа CircularBuffer.
func NewCircularBuffer(size int) CircularBuffer {
	return CircularBuffer{values: make([]float64, size+1)}
}

// ForceSetValueByIdx выставляет значение буфера по индексу.
func (b CircularBuffer) ForceSetValueByIdx(idx int, v float64) {
	// лучше не использовать такой приём на практике, когда параметр метода
	// не указатель, а значение
	b.values[idx] = v
}

func main() {
	buf := NewCircularBuffer(4)
	for i := 0; i < 6; i++ {
		if i > 0 {
			buf.AddValue(float64(i))
		}
		fmt.Printf("[%d]: %v\n", buf.GetCurrentSize(), buf.GetValues())

	}
	buf.ForceSetValueByIdx(0, -1.0)
	buf.ForceSetValueByIdx(1, -2.0)
	fmt.Println(buf.values)
}
