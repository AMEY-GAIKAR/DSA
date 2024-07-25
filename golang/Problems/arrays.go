package problems

func maxInt(a, b int) int {
  if a >= b {
    return a
  } else {
    return b
  }
}

func minInt(a, b int) int {
  if a <= b {
    return a
  } else {
    return b
  }
}

func maxConsecutiveOnes(nums []int) int {
  var localCount int = 0
  var globalCount int = 0
  for i := range(nums) {
    if nums[i] == 1 {
      localCount += 1
    } else {
      localCount = 0
    }
    globalCount = maxInt(localCount, globalCount)
  }
  return globalCount
}
