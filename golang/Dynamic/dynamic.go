package dynamic

func Fibonacci(n int, dp *[]int) int {
  if n <= 1 {
    return n
  }
  if (*dp)[n] != 0 {
    return (*dp)[n]
  }
  (*dp)[n] = Fibonacci(n-1, dp) + Fibonacci(n-2, dp)
  return (*dp)[n]
}
