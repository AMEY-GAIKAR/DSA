package recursion

import "fmt"

func PrintN(s string, n int) {
  if n == 1 {
    return
  } else {
    fmt.Println(s)
    PrintN(s, n - 1)
  }
}

func PrintNumbersI(n int) {
  if n ==0 {
    return
  } else {
    fmt.Println(n)
    PrintNumbersI(n - 1)
  }
}

func PrintNumbersII(n int, c int) {
  if c == n + 1 {
    return
  } else {
    fmt.Println(c)
    PrintNumbersII(n, c + 1)
  }
}

func Addition(n int) int {
  if n == 0 {
    return 0
  } else {
    return n + Addition(n -1)
  }
}

func Factorial(n int) int {
  if n == 0 {
    return 1
  } else {
    return n * Factorial(n - 1)
  }
}
