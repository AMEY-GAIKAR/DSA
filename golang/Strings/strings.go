package strings

import (
	"unicode"
)

func IsPalindrome(s string) bool {
	var left int = 0
	var right int = len(s) - 1
	for left < right {
		if !unicode.IsLetter(rune(s[left])) && !unicode.IsDigit(rune(s[left])) {
			left++
		} else if !unicode.IsLetter(rune(s[right])) && !unicode.IsDigit(rune(s[right])) {
			right--
		} else {
			if unicode.ToLower(rune(s[left])) != unicode.ToLower(rune(s[right])) {
				return false
			}
			left++
			right--
		}
	}
	return true
}
