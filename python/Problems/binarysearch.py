from typing import List

def binary_search_recursive(array: List[int], key: int, beg: int, end: int) -> int:
    if  end >= beg:
        mid: int = (beg + end + 1) // 2 
        if array[mid] == key:
            return mid
        elif key < array[mid]:
            return binary_search_recursive(array, key, beg, mid-1)
        else:
            return binary_search_recursive(array, key, mid+1, end)
    return -1

def binary_search(array: List[int], key: int) -> int:
    start: int = 0
    end: int = len(array) - 1
    while end >= start:
        mid: int = (start + end) // 2
        if array[mid] == key:
            return mid
        elif key < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1 

def searchInsert(array: List[int], key: int) -> int:
    start: int = 0
    end: int = len(array) - 1
    position: int = len(array) - 1
    while end >= start:
        mid: int = (start + end) // 2
        if key <= array[mid]:
            position = mid
            end = mid - 1
        else:
            start = mid + 1
    return position

def lower_bound_BS(array: List[int], key: int) -> int:
    end: int = len(array) - 1
    start: int = 0
    position: int = -1
    while end >= start:
        mid: int = (start + end) // 2
        if key <= array[mid]:
            position = mid
            end = mid - 1
        else:
            start = mid + 1
    return position

def upper_bound_BS(array: List[int], key: int) -> int:
    end: int = len(array) - 1
    start: int = 0
    position: int = len(array)
    while end >= start:
        mid: int = (end + start) // 2
        if key < array[mid]:
            position = mid
            end = mid - 1
        else:
            start = mid + 1
    return position

def floor_BS(array: List[int], key: int) -> int:
    start: int = 0
    end: int = len(array) - 1
    position: int = -1
    while end >= start:
        mid = (start + end) // 2
        if array[mid] <= key:
            position = array[mid]
            start = mid + 1
        else:
            end = mid - 1
    return position

def ceil_BS(array: List[int], key: int) -> int:
    start: int = 0
    end: int = len(array) - 1
    position: int = - 1
    while end >= start:
        mid = (start + end) // 2
        if array[mid] >= key:
            position = array[mid]
            end = mid - 1
        else:
            start = mid + 1
    return position

def sqrt(x: int) -> int:
    if x == 0:
        return 0
    start: int = 1
    end: int = x // 2
    ans: int = 1
    while start <= end:
        mid = (start + end) // 2
        if mid*mid == x:
            return mid
        elif mid*mid > x:
            end = mid - 1
        else:
            start = mid + 1
            ans = mid
    return ans

if __name__ == "__main__":
    print(sqrt(0))
