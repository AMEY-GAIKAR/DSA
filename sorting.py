from typing import List

def BubbleSort(array: List[int]) -> List[int] :
   
    length = len(array)

    for i in range(length):
        for j in range(i+1, length):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array

def SelectionSort(array: List[int]) -> List[int]:

    length = len(array)

    for i in range(length-1):
        min = i
        for j in range(i+1, length):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

    return array

def InsertionSort(array: List[int]) -> List[int] :
    
    length = len(array)

    for i in range(length):
        for j in range(i+1, length):
            while array[j] < array[i]:
                array[j], array[i] = array[i], array[j]

    return array

def QuickSortPartition(array: List[int], low: int, high: int) -> int :
    pivot = array[high]

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[high], array[i+1] = array[i+1], array[high]

    return i + 1
    
def QuickSort(array: List[int], low:int, high: int) -> None :
    if low < high:
        a = QuickSortPartition(array, low, high)

        QuickSort(array, low, a-1)
        QuickSort(array, a+1, high)

