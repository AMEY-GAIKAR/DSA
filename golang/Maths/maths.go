package maths

import "math"

func GCD(a, b int) int {
  var factors []int
  var min int = int(math.Min(float64(a), float64(b)))
  var max int = int(math.Max(float64(a), float64(b)))
  for i := 2; i <= min; i++ {
    if max % i == 0 && min % i == 0 {
      factors = append(factors, i)
    }
  }
  if len(factors) == 0 {
    return 1
  }
  return factors[len(factors)-1]
}

func IsPrime(n int) bool {
  if n == 2 {
    return true
  }
  if n < 2 || n % 2 == 0 {
    return false
  } 
  var i int = 3
  for i * i <= n {
    if n % i == 0 {
      return false
    }
    i += 2
  }
  return true
}

func NthPrime(n int) int {
  if n == 1 {
    return 2
  }
  var prime int = 2
  var count int = 1
  var i int = 3
  for count != n {
    if IsPrime(i) {
      prime = i
      count++
    }
    i += 2
  }
  return prime
}

// func RomanToInteger(str string) int {
//
// }
//
// func IntegerToRoman(n int) string {
//
// }
