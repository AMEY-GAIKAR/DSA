package binarysearch

func BinarySearch(nums []int, key int) int {
  var start = 0
  var end = len(nums) - 1
  for start <= end {
    var mid int = (start + end) / 2
    if nums[mid] == key {
      return mid
    } else if nums[mid] > key {
      end = mid - 1 
    } else {
      start = mid + 1
    }
  }
  return -1
}

func BinarySearchRecursive(nums []int, start, end, key int) int {
  var mid int = (start + end) / 2
  if nums[mid] == key {
    return mid
  } else if nums[mid] > key {
    BinarySearchRecursive(nums, start, end - 1, key)
  } else {
    BinarySearchRecursive(nums, start + 1, end, key)
  }
  return -1
}

func SearchInsertPosition(nums []int, key int) int {
  var start int = 0
  var end int = len(nums) - 1
  var position int = len(nums)
  for start <= end {
    var mid int = (start + end) / 2
    if nums[mid] >= key {
      position = mid
      end = mid - 1
    } else {
      start = mid + 1
    }
  }
  return position
}

func LowerBound(nums []int, key int) int {
  var start int = 0
  var end int = len(nums) - 1
  var answer int = len(nums)
  for start <= end {
    var mid int = (start + end) / 2
    if key >= nums[mid] {
      start = mid + 1
    } else {
      end = mid - 1
      answer = mid
    }
  }
  return answer
}

func Sqrt(x int) int {
  if x == 0 {
    return 0
  }
  var start int = 1
  var end int = x / 2
  var answer int = 1
  for start <= end {
    var mid int = (start + end) / 2
    if mid * mid == x {
      return mid
    } else if mid * mid > x {
      end = mid - 1
    } else {
      answer = mid
      start = mid + 1
    }
  }
  return answer
}
