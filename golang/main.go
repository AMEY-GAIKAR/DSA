package main

import (
	"fmt"

	"github.com/AMEY-GAIKAR/DataStructures/Dynamic" 
)

func main()  {
  dp := make([]int, 7+1)
  res := dynamic.Fibonacci(7, &dp)
  fmt.Println(res)
}
