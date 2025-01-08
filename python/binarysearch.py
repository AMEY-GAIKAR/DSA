from typing import List

def BinarySearch(nums: List[int], key: int) -> int:
    start: int = 0
    end: int = len(nums) - 1
    while start <= end:
        mid: int = (start + end) // 2
        if nums[mid] == key:
            return mid
        elif nums[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1 

def BinarySearchRecursive(nums: List[int], key: int, start: int, end: int) -> int:
    if  end >= start:
        mid: int = (start + end) // 2 
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            return BinarySearchRecursive(nums, key, start, mid - 1)
        else:
            return BinarySearchRecursive(nums, key, mid + 1, end)
    return -1

def BinarySearch2D(matrix: List[List[int]], target: int) -> int:
    rows: int = len(matrix)
    columns: int = len(matrix[0])
    start: int = 0
    end: int = rows * columns - 1
    while start <= end:
        mid: int = (start + end) // 2
        if matrix[mid // columns][mid % columns] == target:
            return True
        elif matrix[mid // columns][mid % columns] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def SearchInsertPosition(nums: List[int], key: int) -> int:
    start: int = 0
    end: int = len(nums) - 1
    position: int = len(nums)
    while end >= start:
        mid: int = (start + end) // 2
        if key <= nums[mid]:
            position = mid
            end = mid - 1
        else:
            start = mid + 1
    return position

def LowerBound(nums: List[int], key: int) -> int:
    end: int = len(nums) - 1
    start: int = 0
    position: int = len(nums)
    while end >= start:
        mid: int = (start + end) // 2
        if key <= nums[mid]:
            position = mid
            end = mid - 1
        else:
            start = mid + 1
    return position

def Sqrt(x: int) -> int:
    if x == 0:
        return 0
    start: int = 1
    end: int = x // 2
    ans: int = 1
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans
