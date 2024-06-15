from typing import Dict, List

def create_freq_table(array: List[int]) -> Dict[int, int]:
    """
    Create a hashmap with the element of the array as the key 
    and its frequency as the value.
    When a new element is encountered, add it to the hashmap
    and set its frequency to 1.
    When an exsisting element is encountered, increase its 
    frequency by 1.
    Time Complexity: O(n) 
    The array is traversed once.
    Space Complexity: O(n)
    Involves the creation of a hashmap with maximum size of n.
    """
    freq: Dict[int, int] = {}
    for i in array:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    return freq

def find_highest_freq(array: List[int]) -> int:
    """
    Create a frequency hashmap of all unique elements.
    Sort the hashmap and return the largest element.
    Time Complexity: O(n) 
    The array is traversed once.
    Space Complexity: O(n)
    Involves the creation of a hashmap with maximum size of n.
    """
    freq: Dict[int, int] = create_freq_table(array)
    return sorted(freq, key=lambda x: freq[x])[-1]

def find_lowest_freq(array: List[int]) -> int:
    freq: Dict[int, int] = create_freq_table(array)
    return sorted(freq, key=lambda x: freq[x])[0]

def find_second_highest_freq(array: List[int]) -> int:
    freq: Dict[int, int] = create_freq_table(array)
    return sorted(freq, key=lambda x: freq[x])[-2]

def largest_element(array: List[int]) -> int:
    """
    Maintain a variable with the current highest value or
    its index.
    Update this variable as the array is traversed.
    Time Complexity: O(n)
    The array is traversed once.
    Space Complexity: O(1)
    A variable must store the value or position of the
    largest element
    """
    largest: int = array[0]
    for i in range(1, len(array)):
        if largest < array[i]:
            largest = array[i]
    return largest

def second_largest_smallest(array: List[int]) -> tuple:
    """
    Create variables for largest, 2nd largest, smallest and
    2nd smallest elements.
    Find the smallest and largest element by iterating over
    the array.
    Iterate over the array again to find the 2nd largest element
    that will be greater than all other elements but just 
    smaller than the largest element.
    Within the same loop find the 2nd smallest element.
    Time Complexity: O(n+n)
    Linear time complexity as the second loop is not contained 
    inside the first loop.
    Space Complexity: O(1)
    """
    largest: int = 0
    second_largest: int = 0
    smallest: float = float('inf')
    second_smallest: float = float('inf')

    for i in range(len(array)):
        if array[i] > largest:
            largest = array[i]
        if array[i] < smallest:
            smallest = array[i]

    for i in range(len(array)):
        if array[i] > second_largest and array[i] < largest:
            second_largest = array[i]
        if array[i] < second_smallest and array[i] > smallest:
            second_smallest = array[i]

    return second_largest, second_smallest

def check_sorted(array: List[int]) -> bool:
    """
    Since the array is sorted, check if an element is equal to 
    or smaller than the next element.
    Time Complexity: O(n)
    The array is traversed once.
    Space Complexity: 1
    No extra space is required.
    """
    for n in range(len(array)-1):
        if array[n] <= array[n+1]:
            continue
        else:
            return False
    return True

def remove_duplicates(array: List[int]) -> set[int]:
    """
    Convert the list/array into a set of unique elements.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    unique: set[int] = set()
    for i in range(len(array)):
        unique.add(array[i])
    return unique

# def remove_duplicates_II(array: List[int]) -> List[int]:
#     i: int = 0
#     for j in range(len(array)):
#         if array[j] 
#
#     return array

def left_rotate(array: List[int], places: int = 1) -> List[int]:
    """
    Create a new list and add elements from old list as:
    new_list[i] = old_list[i+places_to_shift % length_array] 
    Time Complexity: O(n)
    The array is traversed once.
    Space Complexity: O(n)
    A new array of the same length is created.
    """
    new_array: List[int] = [0 for _ in array]
    for i in range(len(array)):
        new_array[i] = array[(i+places)%len(array)]
    return new_array

def left_rotate_inplace(array: List[int]) -> List[int]:
    """
    Stote the first element in a variable.
    Iterate over the list reassigning the variable position as:
    list[i] = list[i+1]
    Finally set the last element of the list as temporary variable.
    Time Complexity: O(n)
    The array is traversed once.
    Space Complexity: 1
    """
    temp: int = array[0]
    for i in range(len(array)-1):
        array[i] = array[i+1]
    array[len(array)-1] = temp
    return array

def union(array_1: List[int], array_2: List[int]) -> List[int]:
    """
    Create a sorted set.
    Iterate over the larger list and add elements from both
    lists into the sorted set.
    Time Complexity: O(n)
    where n is the size of the larger list
    The list is traversed once.
    Space Complexity: O(n)
    Involves creation of a sorted set.
    """
    union: set[int] = set()
    greater: List[int] = max(array_1, array_2)
    smaller: List[int] = min(array_1, array_2)
    for i in range(len(greater)):
        if i >= len(smaller):
            union.add(greater[i])
        else:
            union.add(smaller[i])
            union.add(greater[i])
    return list(union)

def find_missing(array: List[int], n: int) -> float:
    """
    Calculate the sum of 1st n numbers: Sum = n*(n-1)/array_2
    Return the difference of Sum and sum of all elements of the array.
    Time Complexity: O(n)
    Iterate over the array to find the sum of elements.
    Space Complexity: 1
    No extra space is required.
    """
    return n*(n-1)/2 - sum(array)

print(find_missing([1,5,3,4,6], 7))
