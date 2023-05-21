package main

import (
	"fmt"
	"io"
	"os"
)

func CopyFile(srcFileName, dstFileName string) error {
	srcFile, err := os.Open(srcFileName)
	if err != nil {
		return err
	}
	dstFile, err := os.Create(dstFileName)
	if err != nil {
		return err
	}
	n, err := io.Copy(dstFile, srcFile)
	if err != nil {
		return err
	}
	fmt.Printf("Copied %d bytes from %s to %s", n, srcFileName, dstFileName)
	return nil
}
