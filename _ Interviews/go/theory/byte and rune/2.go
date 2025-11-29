package main

import (
	"fmt"
	"unicode"
)

func main() {
	// ----------------------------------------------------------------------
	// 1. BYTE — works for raw data, shows UTF-8 bytes, breaks for Unicode
	// ----------------------------------------------------------------------
	fmt.Println("=== BYTES ===")
	s := "Привет 😊" // Russian + emoji (multi-byte UTF-8)

	// Iterate by BYTE
	for i := 0; i < len(s); i++ {
		fmt.Printf("byte %d: %d\n", i, s[i])
	}
	fmt.Println()

	// Why bytes exist: raw binary data (not characters!)
	raw := []byte{0x89, 0x50, 0x4E, 0x47} // PNG header
	fmt.Println("raw bytes:", raw)
	fmt.Println()

	// ----------------------------------------------------------------------
	// 2. RUNE — correct Unicode characters
	// ----------------------------------------------------------------------
	fmt.Println("=== RUNES ===")

	for i, r := range s {
		fmt.Printf("rune start %2d: %c  (U+%04X)\n", i, r, r)
	}
	fmt.Println()

	// ----------------------------------------------------------------------
	// 3. Example: uppercase first character (must use runes)
	// ----------------------------------------------------------------------
	fmt.Println("=== UPPERCASE EXAMPLE ===")
	name := "иван"
	runes := []rune(name)

	runes[0] = unicode.ToUpper(runes[0])
	fmt.Println("uppercased:", string(runes))
	fmt.Println()

	// ----------------------------------------------------------------------
	// 4. Example: finding digits (must use runes)
	// ----------------------------------------------------------------------
	fmt.Println("=== DIGIT DETECTION ===")
	text := "Цена: 50€ 😊"

	for _, r := range text {
		if unicode.IsDigit(r) {
			fmt.Println("digit:", string(r))
		}
	}
}
