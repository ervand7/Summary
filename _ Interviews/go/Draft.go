package main

import (
	"bytes"
	"io"
)

var data = []struct {
	input  []byte
	output []byte
}{
	{[]byte("abc"), []byte("abc")},
	{[]byte("elvis"), []byte("Elvis")},
	{[]byte("aElvis"), []byte("aElvis")},
	{[]byte("abcelvis"), []byte("abcElvis")},
	{[]byte("eelvis"), []byte("eElvis")},
	{[]byte("aelvis"), []byte("aElvis")},
	{[]byte("aabeeeelvis"), []byte("aabeeeElvis")},
	{[]byte("e l v i s"), []byte("e l v i s")},
	{[]byte("aa bb e l v i saa"), []byte("aa bb e l v i saa")},
	{[]byte(" elvi s"), []byte(" elvi s")},
	{[]byte("elvielvis"), []byte("elviElvis")},
	{[]byte("elvielvielviselvi1"), []byte("elvielviElviselvi1")},
	{[]byte("elvielviselvis"), []byte("elviElvisElvis")},
}

func assembleInputStream() []byte {
	var in []byte
	for _, d := range data {
		in = append(in, d.input...)
	}
	return in
}

func assembleOutputStream() []byte {
	var out []byte
	for _, d := range data {
		out = append(out, d.output...)
	}
	return out
}

func algOne(data []byte, find []byte, repl []byte, output *bytes.Buffer) {
	input := bytes.NewBuffer(data)
	size := len(find)
	buf := make([]byte, size)
	end := size - 1
	if n, err := io.ReadFull(input, buf[:end]); err != nil {
		output.Write(buf[:n])
		return
	}
	for {
		if _, err := io.ReadFull(input, buf[end:]); err != nil {
			output.Write(buf[:end])
			return
		}
		if bytes.Equal(buf, find) {
			output.Write(repl)
			if n, err := io.ReadFull(input, buf[:end]); err != nil {
				output.Write(buf[:n])
				return
			}
			continue
		}
		output.WriteByte(buf[0])
		copy(buf, buf[1:])
	}
}

func algTwo(data []byte, find []byte, repl []byte, output *bytes.Buffer) {
	input := bytes.NewReader(data)
	size := len(find)
	idx := 0
	for {
		b, err := input.ReadByte()
		if err != nil {
			break
		}
		if b == find[idx] {
			idx++
			if idx == size {
				output.Write(repl)
				idx = 0
			}
			continue
		}
		if idx != 0 {
			output.Write(find[:idx])
			input.UnreadByte()
			idx = 0
			continue
		}
		output.WriteByte(b)
		idx = 0
	}
}
