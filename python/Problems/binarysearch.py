from typing import List

def binary_search(array: List[int], key: int, beg: int, end: int) -> int:
    """"""
    if  end >= beg:
        mid: int = (beg + end + 1) // 2 
        if array[mid] == key:
            return mid
        elif key < array[mid]:
            return binary_search(array, key, beg, mid-1)
        else:
            return binary_search(array, key, mid+1, end)
    return -1

def lower_bound_BS(array: List[int], key: int) -> int:
    end: int = len(array) - 1
    start: int = 0
    position: int = 0
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
        if key > array[mid]:
            position = mid
            start = mid + 1
        else:
            end = mid - 1
    return position + 1

if __name__ == "__main__":
    print()
