// Package hamming ..
package hamming

import (
	"errors"
)

// Distance Calculate the hamming distance between two DNA strands(strings)
func Distance(str1, str2 string) (int, error) {
	if len(str1) != len(str2) {
		return 0, errors.New("true")
	}
	count := 0
	for index := range str1 {
		if str1[index] != str2[index] {
			count++
		}
	}
	return count, nil
}
