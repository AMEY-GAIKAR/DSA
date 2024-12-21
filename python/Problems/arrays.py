from typing import Dict, List

def maxInt(a: int, b: int) -> int:
    if a > b:
        return a
    return b

def minInt(a: int, b: int) -> int:
    if a < b:
        return a
    return b

def Reverse(nums: List[int]) -> List[int]:
    i: int = 0
    j: int = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i = i + 1
        j = j - 1
    return nums

def LinearSearch(nums: List[int], key: int) -> int:
    for i, v in enumerate(nums):
        if v == key:
            return i
    return -1

def SearchRange(nums: List[int], key: int) -> List[int]:
    answer: List[int] = [-1, -1]
    for i in range(len(nums)):
        if nums[i] == key:
            answer[0] = i
            break
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == key:
            answer[1] = i
            break
    return answer

def CreateFrequencyTable(nums: List[int]) -> Dict[int, int]:
    freq: Dict[int, int] = {}
    for i in nums:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    return freq

def FindHighestFrequency(nums: List[int]) -> int:
    freq: Dict[int, int] = CreateFrequencyTable(nums)
    return sorted(freq, key=lambda x: freq[x])[-1]

def FindLowestFrequency(nums: List[int]) -> int:
    freq: Dict[int, int] = CreateFrequencyTable(nums)
    return sorted(freq, key=lambda x: freq[x])[0]

def FindSecondHighestFrequency(nums: List[int]) -> int:
    freq: Dict[int, int] = CreateFrequencyTable(nums)
    return sorted(freq, key=lambda x: freq[x])[-2]

def FindSecondLowestFrequency(nums: List[int]) -> int:
    freq: Dict[int, int] = CreateFrequencyTable(nums)
    return sorted(freq, key=lambda x: freq[x])[1]

def FindLargest(nums: List[int]) -> int:
    largest: int = nums[0]
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    return largest

def FindSmallest(nums: List[int]) -> int:
    smallest: int = nums[0]
    for i in range(len(nums)):
        if nums[i] > smallest:
            smallest = nums[i]
    return smallest

def FindSecondLargest(nums: List[int]) -> int:
    largest: int = 0
    second_largest: int = 0
    for i in range(len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        if nums[i] > second_largest and nums[i] < largest:
            second_largest = nums[i]

    return second_largest

def FindSecondSmallest(nums: List[int]) -> int:
    smallest: int = nums[0]
    second_smallest: int = nums[0] 
    for i in range(len(nums)):
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]    
        if nums[i] < second_smallest and nums[i] > smallest:
            second_smallest = nums[i]
    return second_smallest


def Leaders(nums: List[int]) -> List[int]:
    leader: int = nums[-1]
    leaders: List[int] = []
    for i in range(len(nums)-1, -1, -1):
        if nums[i] >= leader:
            leader = nums[i]
            leaders.append(nums[i])
    leaders.reverse()
    return leaders

def FindSingleI(nums: List[int]) -> int:
    frequencyTable: Dict[int, int] = {}
    for i in range(len(nums)):
        if nums[i] in frequencyTable:
            frequencyTable[nums[i]] = frequencyTable[nums[i]] + 1
        else:
            frequencyTable[nums[i]] = 1
    for i in frequencyTable:
        if frequencyTable[i] == 1:
            return i
    return -1

def FindSingleII(nums: List[int]) -> int:
    freq: Dict[int, int] = CreateFrequencyTable(nums)
    return sorted(freq, key=lambda x: freq[x])[0]

def FindSingleIII(nums: List[int]) -> int:
    xorSum: int = 0
    for _, v in enumerate(nums):
        xorSum = xorSum ^ v
    return xorSum

def CheckSorted(nums: List[int]) -> bool:
    for n in range(len(nums)-1):
        if nums[n] <= nums[n+1]:
            continue
        else:
            return False
    return True

def CheckRotatedSorted(nums: List[int]) -> bool:
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

def FindEvenDigits(nums: List[int]) -> int:
    pass

def MaxConsecutiveOnes(nums: List[int]) -> int:
    count: int = 0
    temp: int = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            temp += 1
        else:
            temp = 0
        count = max(count, temp)
    return count

def FindMissing(nums: List[int]) -> float:
    n: int = len(nums)
    return n*(n+1)/2 - sum(nums)

def TwoSumI(nums: List[int], sum: int) -> List[int]:
    for i in range(len(nums)):
        target: int = sum - nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == target:
                return [nums[i], nums[j]]
    return [-1, -1]

def TwoSumII(nums: List[int], target: int) -> List[int]:
    map: Dict[int, int] = {}
    for i in range(len(nums)):
        if target-nums[i] in map: 
            return [i, map[target-nums[i]]]
        map[nums[i]] = i
    return [-1, -1]

def RemoveDuplicatesI(nums: List[int]) -> List[int]:
    unique: set[int] = set()
    for i in range(len(nums)):
        unique.add(nums[i])
    return list(unique)

def RemoveDuplicatesII(nums: List[int]) -> List[int]:
    i: int = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return nums

def RemoveZeros(nums: List[int]) -> List[int]:
    i: int = 0
    for j in range(len(nums)): 
        if nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

def ContainsDuplicate(nums: List[int]) -> bool:
    values: set[int] = set()
    for i in range(len(nums)):
        if nums[i] not in values:
            values.add((nums[i]))
        else:
            return True
    return False

# TODO
def LeftRotateK(nums: List[int]) -> List[int]:
    temp: int = nums[0]
    for i in range(len(nums)-1):
        nums[i] = nums[i+1]
    nums[len(nums)-1] = temp
    return nums
# TODO 
def RightRotateK(nums: List[int], k: int) -> List[int]:
    k = k % len(nums)
    temp: List[int] = [0] * k
    for i in range(k):
        temp[i] = nums[i]
    j: int = 0
    for i in range(k, len(nums)):
        nums[j] = nums[i]
        j += 1
    n: int = 0
    for i in range(k):
        nums[k+i+2] = temp[n]
        n += 1
    return nums

def LowerBound(nums: List[int], key: int) -> int:
    for i in range(len(nums)):
        if nums[i] > key:
            return i-1
        elif nums[i] == key:
            return i
    return len(nums)

def SortColours(nums: List[int]) -> List[int]:
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

def MajorityElementI(nums: List[int]) -> int:
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

def MaxSubArraySum(nums: List[int]) -> int:
    sum: int = 0
    maxSum = int(-float('inf'))
    for i in range(len(nums)):
        sum = max(nums[i], sum + nums[i])
        maxSum = max(maxSum, sum)
    return maxSum

def MaxProfit(prices: List[int]) -> int:
    minimum: int = prices[0]
    diff: int = 0
    for i in range(len(prices)):
        minimum = min(minimum, prices[i]) 
        diff = max(diff, prices[i]-minimum)
    return diff

def RearrangeBySign(nums: List[int]) -> List[int]:
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

def Merge(nums1: List[int], nums2: List[int], m: int, n: int):
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

def UnionI(nums1: List[int], nums2: List[int]) -> List[int]:
    s1: set[int] = set(nums1)
    s2: set[int] = set(nums2)
    return sorted(list(s1.union(s2)))

def LargestAltitude(gain: List[int]) -> int:
    altitude: List[int] = [0] * (len(gain) + 1)
    for i in range(len(gain)):
        altitude[i+1] = altitude[i] + gain[i]
    return max(altitude)

def FindPivotIndex(nums: List[int]) -> int:
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i+1
    return 0

def DiagonalSum(mat: List[List[int]]) -> int:
    sum: int = 0
    dim: int = len(mat)
    for n in range(dim):
        sum += mat[n][n]
    for n in range(dim - 1, -1, -1):
        sum += mat[dim - n - 1][n]
    if dim % 2 != 0:
        sum -= mat[dim // 2][dim // 2]
    return sum

def KthFactor(n: int, k: int) -> int:
    factors: List[int] = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors[k-1]

def LongestConsecutiveSubSequence(nums: List[int]) -> int:
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

def SetMatrixZeros(matrix: List[List[int]]) -> List[List[int]]:
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
