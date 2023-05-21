package Divide

import "errors"

func Divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("ZeroDivisionError")
	}
	return a / b, nil
}
