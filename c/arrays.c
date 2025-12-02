#include <limits.h>
#include <malloc.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int maxInt(int a, int b) {
  if (a > b) {
    return a;
  }
  return b;
}

int minInt(int a, int b) {
  if (a < b) {
    return a;
  }
  return b;
}

void Reverse(int nums[], size_t size) {
  int i = 0;
  int j = size - 1;
  while (i < j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
    i++;
    j--;
  }
}

struct CounterItem {
    int Item;
    int Count;
};

bool SearchCounter(struct CounterItem *counter, int cSize, int key) {
  for (int i = 0; i < cSize; i++) {
    if (counter[i].Item == key) {
      return true;
    }
  }
  return false;
}

void AddCounterItem(struct CounterItem **counter, int *cSize, int key) {
  *counter = realloc(*counter, (*cSize + 1) * sizeof(struct CounterItem));
  if (*counter == NULL) {
    exit(EXIT_FAILURE);
  }
  (*counter)[*cSize].Item = key;
  (*counter)[*cSize].Count = 1;
  (*cSize)++;
}

void IncrementCounter(struct CounterItem *counter, int cSize, int key) {
  for (int i = 0; i < cSize; i++) {
    if (counter[i].Item == key) {
      counter[i].Count++;
    }
  }
}

struct CounterItem *CreateCounter(int nums[], size_t size, int *cSize) {
  struct CounterItem *counter =
      (struct CounterItem *)malloc(sizeof(struct CounterItem));
  *cSize = 0;
  for (int i = 0; i < size; i++) {
    if (SearchCounter(counter, *cSize, nums[i]) == true) {
      IncrementCounter(counter, *cSize, nums[i]);
    } else {
      AddCounterItem(&counter, cSize, nums[i]);
    }
  }
  return counter;
}

int LinearSearch(int nums[], size_t size, int key) {
  for (int i = 0; i < size; i++) {
    if (nums[i] == key) {
      return i;
    }
  }
  return -1;
}

int *SearchRange(int nums[], size_t size, int key, int *returnSize) {
  int *answer = (int *)malloc(sizeof(int) * 2);
  *returnSize = 2;
  answer[0] = -1;
  answer[1] = -1;
  for (int i = 0; i < size; i++) {
    if (nums[i] == key) {
      answer[0] = i;
      break;
    }
  }
  for (int j = size - 1; j > 0; j--) {
    if (nums[j] == key) {
      answer[1] = j;
      break;
    }
  }
  return answer;
}

int FindHighestFrequency(int nums[], size_t size) {
  int answer, count;
  count = INT_MIN;
  int cSize = 0;
  struct CounterItem *c = CreateCounter(nums, size, &cSize);
  for (int i = 0; i < cSize; i++) {
    if (c[i].Count > count) {
      answer = c[i].Item;
      count = c[i].Count;
    }
  }
  return answer;
}

int FindLowestFrequency(int nums[], size_t size) {
  int answer, count;
  count = INT_MAX;
  int cSize = 0;
  struct CounterItem *c = CreateCounter(nums, size, &cSize);
  for (int i = 0; i < cSize; i++) {
    if (c[i].Count < count) {
      answer = c[i].Item;
      count = c[i].Count;
    }
  }
  return answer;
}

int FindLargest(int nums[], size_t size) {
  int largest = nums[0];
  for (int i = 0; i < size; i++) {
    if (nums[i] > largest) {
      largest = nums[i];
    }
  }
  return largest;
}

int FindSmallest(int nums[], size_t size) {
  int smallest = nums[0];
  for (int i = 0; i < size; i++) {
    if (nums[i] < smallest) {
      smallest = nums[i];
    }
  }
  return smallest;
}

int FindSecondLargest(int nums[], size_t size) {
  int largest = nums[0];
  int secondLargest = nums[0];
  for (int i = 0; i < size; i++) {
    if (nums[i] < largest) {
      largest = nums[i];
    }
    if (nums[i] > largest && nums[i] < secondLargest) {
      secondLargest = nums[i];
    }
  }
  return secondLargest;
}

int FindSecondSmallest(int nums[], size_t size) {
  int smallest = nums[0];
  int secondSmallest = nums[0];
  for (int i = 0; i < size; i++) {
    if (nums[i] < smallest) {
      smallest = nums[i];
    }
    if (nums[i] > smallest && nums[i] < secondSmallest) {
      secondSmallest = nums[i];
    }
  }
  return secondSmallest;
}

int *Leaders(int nums[], size_t size, int *returnSize) {
  int *answer = (int *)malloc(sizeof(int) * size);
  int max = nums[size - 1];
  answer[0] = max;
  int index = 1;
  for (int i = size - 2; i >= 0; i--) {
    if (nums[i] >= max) {
      max = nums[i];
      answer[index] = nums[i];
      index++;
    }
  }
  *returnSize = index;
  Reverse(answer, *returnSize);
  return answer;
}

int FindSingleI(int nums[], size_t size) {
  int cSize = 0;
  struct CounterItem *c = CreateCounter(nums, size, &cSize);
  for (int i = 0; i < cSize; i++) {
    if (c[i].Count == 1) {
      return c[i].Item;
    }
  }
  return 0;
}

int FindSingleII(int nums[], size_t size) {
  int xorSum = 0;
  for (int i = 0; i < size; i++) {
    xorSum = xorSum ^ nums[i];
  }
  return xorSum;
}

bool CheckSorted(int nums[], size_t size) {
  for (int i = 0; i < size - 1; i++) {
    if (nums[i] > nums[i + 1]) {
      return false;
    }
  }
  return true;
}

bool CheckRotatedSorted(int nums[], size_t size) {
  int count = 0;
  for (int i = 1; i < size; i++) {
    if (nums[i] < nums[i - 1]) {
      count++;
    }
  }
  if (count == 0 || count == 1 && nums[0] > nums[size - 1]) {
    return true;
  }
  return false;
}

int FindEvenDigits(int nums[], size_t size) {
  int answer = 0;
  for (int i = 0; i < size; i++) {
    int digitCount = 0;
    int digit = nums[i];
    while (digit > 0) {
      digit = digit / 10;
      digitCount++;
    }
    if (digitCount % 2 == 0) {
      answer++;
    }
  }
  return answer;
}

int MaxConsecutiveOnes(int nums[], size_t size) {
  int localCount = 0;
  int globalCount = 0;
  for (int i = 0; i < size; i++) {
    if (nums[i] == 1) {
      localCount++;
    } else {
      localCount = 0;
    }
    globalCount = maxInt(globalCount, localCount);
  }
  return globalCount;
}

int FindMissing(int nums[], size_t size) {
  int sum = 0;
  int n = size;
  for (int i = 0; i < size; i++) {
    sum += nums[i];
  }
  return n * (n + 1) / 2 - sum;
}

int *TwoSumI(int nums[], size_t size, int target, int *returnSize) {
  int *answer = (int *)malloc(sizeof(int) * 2);
  *returnSize = 2;
  answer[0] = -1;
  answer[1] = -1;
  for (int i = 0; i < size; i++) {
    for (int j = i + 1; j < size; j++) {
      if (nums[i] + nums[j] == target) {
        answer[0] = nums[i];
        answer[1] = nums[j];
        return answer;
      }
    }
  }
  return answer;
}

int RemoveDuplicates(int nums[], size_t size) {
  int i = 0;
  for (int j = 1; j < size; j++) {
    if (nums[i] != nums[j]) {
      i++;
      nums[i] = nums[j];
    }
  }
  return i + 1;
}

int RemoveZeros(int nums[], size_t size) {
  int i = 0;
  for (int j = 0; j < size; j++) {
    if (nums[j] != 0) {
      int temp = nums[j];
      nums[j] = nums[i];
      nums[i] = temp;
      i++;
    }
  }
  return i + 1;
}

bool ContainsDuplicates(int nums[], size_t size) {
  int cSize = 0;
  struct CounterItem *c = CreateCounter(nums, size, &cSize);
  for (int i = 0; i < cSize; i++) {
    if (c[i].Count > 1) {
      return true;
    }
  }
  return false;
}

void RightRotateByOne(int nums[], size_t size) {
  if (size == 1) {
    return;
  }
  int temp = nums[size - 1];
  for (int i = size - 1; i >= 0; i--) {
    nums[i] = nums[i - 1];
  }
  nums[0] = temp;
}

void RotateByK(int nums[], size_t size, int k) {
  k = k % size;
  int i = 0;
  int j = size - 1;
  while (i <= j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
    i++;
    j--;
  }
  i = 0;
  j = k - 1;
  while (i <= j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
    i++;
    j--;
  }
  i = k;
  j = size - 1;
  while (i <= j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
    i++;
    j--;
  }
}

int LowerBound(int nums[], size_t size, int target) {
  int start = 0;
  int end = size - 1;
  int answer = size;
  while (start <= end) {
    int mid = (start + end) / 2;
    if (nums[mid] >= target) {
      answer = mid;
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return answer;
}

void SortColors(int nums[], size_t size) {
  int low, mid;
  low = mid = 0;
  int high = size - 1;
  while (mid <= high) {
    if (nums[mid] == 0) {
      int temp = nums[mid];
      nums[mid] = nums[low];
      nums[low] = temp;
      low++;
      mid++;
    } else if (nums[mid] == 2) {
      int temp = nums[mid];
      nums[mid] = nums[high];
      nums[high] = temp;
      high--;
    } else {
      mid++;
    }
  }
}

int MajorityElementI(int nums[], size_t size) {
  int count = 0;
  int element = nums[0];
  for (int i = 0; i < size; i++) {
    if (nums[i] == element) {
      count++;
    } else if (count == 0) {
      element = nums[i];
      count++;
    } else {
      count--;
    }
  }
  return element;
}

int *MajorityElementII(int nums[], size_t size, int *returnSize) {
  int c1 = 0;
  int c2 = 0;
  int e1 = 0;
  int e2 = 0;
  for (int i = 0; i < size; i++) {
    if (nums[i] == e1) {
      c1++;
    } else if (nums[i] == e2) {
      c2++;
    } else if (c1 == 0) {
      e1 = nums[i];
      c1 = 1;
    } else if (c2 == 0) {
      e2 = nums[i];
      c2 = 1;
    } else {
      c1--;
      c2--;
    }
  }
  c1 = 0;
  c2 = 0;
  for (int i = 0; i < size; i++) {
    if (nums[i] == e1) {
      c1++;
    } else if (nums[i] == e2) {
      c2++;
    }
  }
  int *answer = (int *)malloc(sizeof(int) * 2);
  *returnSize = 0;
  if (c1 > size / 3) {
    answer[(*returnSize)++] = e1;
  }
  if (c2 > size / 3) {
    answer[(*returnSize)++] = e2;
  }
  return answer;
}

int MaxSubarraySumI(int nums[], size_t size) {
  int globalSum = INT_MIN;
  int localSum = 0;
  for (int i = 0; i < size; i++) {
    localSum = maxInt(nums[i], nums[i] + localSum);
    globalSum = maxInt(globalSum, localSum);
  }
  return globalSum;
}

int *MaxSubarraySumII(int nums[], size_t size, int *returnSize) {
  int globalSum = INT_MIN;
  int localSum = 0;
  int start = 0;
  int end = 0;
  *returnSize = 2;
  for (int i = 0; i < size; i++) {
    if (localSum == 0) {
      start = i;
    }
    localSum += nums[i];
    if (localSum > globalSum) {
      globalSum = localSum;
      end = i;
    }
    if (localSum <= 0) {
      localSum = 0;
    }
  }
  int *answer = (int *)malloc(sizeof(int) * 2);
  answer[0] = start;
  answer[1] = end;
  return answer;
}

int MaxProfit(int *prices, int pricesSize) {
  int diff = -1;
  int min = INT_MAX;
  for (int i = 0; i < pricesSize; i++) {
    min = minInt(min, prices[i]);
    diff = maxInt(diff, prices[i] - min);
  }
  return diff;
}

int *RearrangeBySign(int *nums, int size, int *returnSize) {
  int *answer = (int *)malloc(sizeof(int) * size);
  *returnSize = size;
  int positive = 0;
  int negative = 1;
  for (int i = 0; i < size; i++) {
    if (nums[i] >= 0) {
      answer[positive] = nums[i];
      positive += 2;
    } else {
      answer[negative] = nums[i];
      negative += 2;
    }
  }
  return answer;
}

void Merge(int nums1[], int nums2[], size_t size1, size_t size2) {
  int i = size1 - 1;
  int j = size2 - 1;
  int k = size1 + size2 - 1;
  while (i >= 0 && j >= 0) {
    if (nums1[i] > nums2[j]) {
      nums1[k] = nums1[i];
      i--;
    } else {
      nums1[k] = nums2[j];
      j--;
    }
    k--;
  }
  while (j >= 0) {
    nums1[k] = nums2[j];
    j--;
    k--;
  }
}
