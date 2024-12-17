from typing import Dict, List

def create_freq_table(array: List[int]) -> Dict[int, int]:
    freq: Dict[int, int] = {}
    for i in array:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    return freq

def find_highest_freq(array: List[int]) -> int:
    freq: Dict[int, int] = create_freq_table(array)
    return sorted(freq, key=lambda x: freq[x])[-1]

def find_lowest_freq(array: List[int]) -> int:
    freq: Dict[int, int] = create_freq_table(array)
    return sorted(freq, key=lambda x: freq[x])[0]

def find_second_highest_freq(array: List[int]) -> int:
    freq: Dict[int, int] = create_freq_table(array)
    return sorted(freq, key=lambda x: freq[x])[-2]

def largest_element(array: List[int]) -> int:
    largest: int = array[0]
    for i in range(1, len(array)):
        if largest < array[i]:
            largest = array[i]
    return largest

def second_largest_smallest(array: List[int]) -> tuple:
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
    for n in range(len(array)-1):
        if array[n] <= array[n+1]:
            continue
        else:
            return False
    return True

def checkRotatedSorted(nums: List[int]) -> bool:
    count: int = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            count += 1
    if count == 0:
        return True
    elif count == 1 and nums[0] >= nums[-1]:
        return True
    else:
        return False

def remove_duplicates(array: List[int]) -> set[int]:
    unique: set[int] = set()
    for i in range(len(array)):
        unique.add(array[i])
    return unique

def remove_duplicates_II(array: List[int]) -> List[int]:
    i: int = 0
    for j in range(len(array)):
        if array[i] != array[j]:
            i += 1
            array[i] = array[j]
    return array

def left_rotate(array: List[int], places: int = 1) -> List[int]:
    new_array: List[int] = [0 for _ in array]
    for i in range(len(array)):
        new_array[i] = array[(i+places)%len(array)]
    return new_array

def left_rotate_inplace(array: List[int]) -> List[int]:
    temp: int = array[0]
    for i in range(len(array)-1):
        array[i] = array[i+1]
    array[len(array)-1] = temp
    return array

def right_rotate_k(nums: List[int], k: int) -> List[int]:
    k = k % len(nums)
    temp: List[int] = [0] * k
    for i in range(k):
        temp[i] = nums[i]
    print(temp)
    j: int = 0
    for i in range(k, len(nums)):
        nums[j] = nums[i]
        j += 1
    print(nums)
    n: int = 0
    for i in range(k):
        print(nums[i], temp[n])
        nums[k+i+2] = temp[n]
        n += 1
    return nums


def unionI(array_1: List[int], array_2: List[int]) -> List[int]:
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

def unionII(array_1: List[int], array_2: List[int]) -> List[int]:
    s1: set[int] = set(array_1)
    s2: set[int] = set(array_2)
    return sorted(list(s1.union(s2)))

def find_missing(array: List[int], n: int) -> float:
    return n*(n+1)/2 - sum(array)

def remove_zeros(array: List[int]) -> List[int]:
    for i in range(len(array)): 
        if array[i] == 0:
            for j in range(i+1, len(array)):
                if array[j] != 0:
                    array[i], array[j] = array[j], array[i]
                    break
    return array

def maximum_ones(nums: List[int]) -> int:
    count: int = 0
    i: int = 0
    temp: int = 0
    while i < len(nums):
        if nums[i] == 1:
            j: int = i + 1
            temp: int = 1
            while j < len(nums) and nums[j] == 1:
                temp += 1
                j += 1
                count = max(temp, count)
        i = temp + i + 1
        temp = 0
    return count

def maximum_ones_II(array: List[int]) -> int:
    count: int = 0
    temp: int = 0
    for i in range(len(array)):
        if array[i] == 1:
            temp += 1
        else:
            temp = 0
        count = max(count, temp)
    return count

def return_once(array: List[int]) -> int:
    freq: Dict[int, int] = create_freq_table(array)
    return sorted(freq, key=lambda x: freq[x])[0]

def two_sum(array: List[int], sum: int) -> List[int]:
    for i in range(len(array)):
        target: int = sum - array[i]
        for j in range(i+1, len(array)):
            if array[j] == target:
                return [array[i], array[j]]
    return [-1, -1]

def two_sum_II(array: List[int], sum: int) -> List[int]:
    for i in range(len(array)):
        position: int = binary_search(array[i+1:], sum-array[i], i, len(array[i+1:])-1)
        if position >= 0:  
            return [i, position]
    return [-1, -1]

def two_sum_hashmap(array: List[int], target: int) -> List[int]:
    map: Dict[int, int] = {}
    for i in range(len(array)):
        if target-array[i] in map: 
            return [i, map[target-array[i]]]
        map[array[i]] = i
    return [-1, -1]

def binary_search(array: List[int], key: int, beg: int, end: int) -> int:
    if  end >= beg:
        mid: int = (beg + end + 1) // 2 
        if array[mid] == key:
            return mid
        elif key < array[mid]:
            return binary_search(array, key, beg, mid-1)
        else:
            return binary_search(array, key, mid+1, end)
    return -1

def lower_bound(array: List[int], key: int) -> int:
    for i in range(len(array)):
        if array[i] > key:
            return i-1
        elif array[i] == key:
            return i
    return len(array)

def upper_bound(array: List[int], key: int) -> int:
    for i in range(len(array)-1, 0, -1):
        if array[i] <= key:
            return i
    return 0

def largestAltitude(gain: List[int]) -> int:
    altitude: List[int] = [0] * (len(gain)+1)
    for i in range(len(gain)):
        altitude[i+1] = altitude[i] + gain[i]
    return max(altitude)

def containsDuplicate(array: List[int]) -> bool:
    values: set[int] = set()
    for i in range(len(array)):
        if array[i] not in values:
            values.add((array[i]))
        else:
            return True
    return False

def findPivotIndex(array: List[int]) -> int:
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return i+1
    return 0

def containsDuplicate_II(nums: List[int], k: int) -> bool:
    i: int = 0
    while i < len(nums):
        values: set[int] = set()
        for n in range(i, min(len(nums), i+k+1)):
            if nums[n] not in values:
                values.add(nums[n])
            else:
                return True
        i += 1
    return False

def merge(nums1: List[int], nums2: List[int], m: int, n: int):
    i: int = m - 1
    j: int = n - 1
    k: int = m + n -1
    while j >= 0:
        if nums2[j] < nums1[i] and i >= 0:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
    return nums1

def diagonalSum(mat: List[List[int]]) -> int:
    sum: int = 0
    dim = len(mat)
    for n in range(dim):
        sum += mat[n][n]
    for n in range(dim-1, -1, -1):
        sum += mat[dim-n-1][n]
    if dim % 2 != 0:
        sum -= mat[dim//2][dim//2]
    return sum

def kthFactor(n: int, k: int) -> int:
    factors: List[int] = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    if len(factors) < k:
        return -1
    return factors[k-1]

def sortArray012(nums: List[int]) -> List[int]:
    left: int = 0
    right: int = len(nums) - 1
    mid: int = 0    
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
    return nums

def majorityElement(nums: List[int]) -> int:
    count: int = 0
    element: int = nums[0]
    for i in range(len(nums)):
        if count == 0:
            element = nums[i]
            count += 1
        elif nums[i] == element:
            count += 1
        elif nums[i] != element:
            count -= 1
    return element

def maxSubArraySum(nums: List[int]) -> int:
    sum: int = 0
    maxSum = int(-float('inf'))
    for i in range(len(nums)):
        sum = max(nums[i], sum + nums[i])
        maxSum = max(maxSum, sum)
    return maxSum

def maxProfit(prices: List[int]) -> int:
    minimum: int = prices[0]
    diff: int = 0
    for i in range(len(prices)):
        minimum = min(minimum, prices[i]) 
        diff = max(diff, prices[i]-minimum)
    return diff

def rearrangeBySign(nums: List[int]) -> List[int]:
    newNums: List[int] = [0] * len(nums)
    even: int = 0
    odd: int = 1
    for i in range(len(nums)):
        if nums[i] < 0:
            newNums[odd] = nums[i]
            odd += 2
        else:
            newNums[even] = nums[i]
            even += 2
    return newNums

def arrayLeaders(nums: List[int]) -> List[int]:
    leader: int = nums[-1]
    leaders: List[int] = []
    for i in range(len(nums)-1, -1, -1):
        if nums[i] >= leader:
            leader = nums[i]
            leaders.append(nums[i])
    leaders.reverse()
    return leaders

def longestConsecutiveSubSequence(nums: List[int]) -> int:
    maxLen: int = 0
    length: int = 0
    s: set[int] = set(nums)
    for i in nums:
        if i-1 not in s:
            j: int = i + 1
            length = 1
            while j in s:
                j += 1
                length += 1
            maxLen = max(maxLen, length)
    return maxLen

def setMatrixZeros(matrix: List[List[int]]) -> List[List[int]]:
    rows: List[int] =  []
    columns: List[int] = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                columns.append(j)
    for i in range(len(rows)):
        matrix[rows[i]] = [0] * len(matrix[0])
    for j in range(len(columns)):
        for k in range(len(matrix)):
            matrix[k][columns[j]] = 0
    return matrix
