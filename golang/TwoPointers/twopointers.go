package twopointers

import (
	"math"
)

func MaxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func MinInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func ViewWindowSizeK(nums []int, k int) [][]int {
	if k > len(nums) || k <= 0 {
		return [][]int{}
	}
	var result [][]int
	var left int = 0
	var right int = k - 1
	for right < len(nums) {
		result = append(result, nums[left:right+1])
		left++
		right++
	}
	return result
}

func MaxWindowSum(nums []int, k int) int {
	if k > len(nums) || k <= 0 {
		return -1
	}
	var max int = math.MinInt
	var sum int = 0
	var left int = 0
	var right int = k - 1
	for i := 0; i < k; i++ {
		sum += nums[i]
	}
	max = MaxInt(max, sum)
	for right < len(nums)-1 {
		sum -= nums[left]
		left++
		right++
		sum += nums[right]
		max = MaxInt(sum, max)
	}
	return max
}

func MinWindowSum(nums []int, k int) int {
	if k > len(nums) || k <= 0 {
		return math.MaxInt
	}
	var min int = math.MaxInt
	var sum int = 0
	var left int = 0
	var right int = k - 1
	for i := 0; i < k; i++ {
		sum += nums[i]
	}
	for right < len(nums)-1 {
		sum -= nums[left]
		left++
		right++
		sum += nums[right]
		min = MinInt(sum, min)
	}
	return min
}

func LongestSubArrayWithSumLessThanK(nums []int, k int) int {
	var maxLength int = 0
	var left int = 0
	var right int = 0
	var sum int = 0
	for right < len(nums) {
		sum += nums[right]
		for sum > k {
			sum -= nums[left]
			left++
		}
		if sum <= k {
			maxLength = MaxInt(maxLength, right-left+1)
		}
		right++
	}
	return maxLength
}

func MaxScore(nums []int, k int) int {
	var right int = len(nums) - 1
	var rSum int = 0
	var lSum int = 0
	var maxSum int = 0
	for i := 0; i < k; i++ {
		lSum += nums[i]
	}
	maxSum = lSum
	for i := k - 1; i >= 0; i-- {
		rSum += nums[right]
		lSum -= nums[i]
		right--
		maxSum = MaxInt(maxSum, lSum+rSum)
	}
	return maxSum
}

func LongestSubstring(s string) int {
	hashMap := make(map[byte]int)
	var left int = 0
	var right int = 0
	maxLength := 0
	for right < len(s) {
		if _, ok := hashMap[s[right]]; ok {
			for left < right && hashMap[s[right]] == 1 {
				delete(hashMap, s[left])
				left++
			}
		}
		hashMap[s[right]] = 1
		maxLength = MaxInt(maxLength, right-left+1)
		right++
	}
	return maxLength
}

func MaximumOnesIII(nums []int, k int) int {
	left, right, zeros, maxLength := 0, 0, 0, 0
	for right < len(nums) {
		if nums[right] == 0 {
			zeros++
			for zeros > k {
				if nums[left] == 0 {
					zeros--
				}
				left++
			}
		}
		maxLength = MaxInt(maxLength, right-left+1)
		right++
	}
	return maxLength
}

func MaximumOnesIIII(nums []int, k int) int {
	var left, right, zeros, maxLength int = 0, 0, 0, 0
	for right < len(nums) {
		if nums[right] == 0 {
			zeros++
		}
		if zeros > k {
			if nums[left] == 0 {
				zeros--
			}
			left++
		}
		if zeros <= k {
			maxLength = MaxInt(maxLength, right-left+1)
		}
		right++
	}
	return maxLength
}

func TwoSumII(nums []int, target int) [2]int {
	var left, right int = 0, len(nums) - 1
	for left < right {
		if nums[left]+nums[right] == target {
			return [2]int{left, right}
		} else if nums[left]+nums[right] < target {
			left++
		} else {
			right--
		}
	}
	return [2]int{-1, -1}
}
