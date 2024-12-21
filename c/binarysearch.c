#include <malloc.h>
#include <stdbool.h>

int BinarySearch(int array[], size_t size, int key) {
  int start = 0;
  int end = size - 1;
  while (start <= end) {
    int mid = (start + end) / 2;
    if (array[mid] == key) {
      return mid;
    } else if (array[mid] > key) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return -1;
}

int BinarySearchRecursive(int nums[], size_t size, int start, int end, int key) {
  int mid = (start + end) / 2;
  if (nums[mid] == key) {
    return mid;
  } else if (nums[mid] > key) {
    BinarySearchRecursive(nums, size, start, mid - 1, key);
  } else {
    BinarySearchRecursive(nums, size, mid + 1, end, key);
  }
  return -1;
}

bool BinarySearch2D(int** matrix, int matrixSize, int* matrixColSize, int target) {
  int start = 0;
  int end = matrixSize * (*matrixColSize) - 1;
  while (start <= end) {
    int mid = (start + end) / 2;
    if (matrix[mid / *(matrixColSize)][mid % *(matrixColSize)] == target) {
      return true;
    } else if (matrix[mid / *(matrixColSize)][mid % *(matrixColSize)] > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return false;
}

int SearchInsertPosition(int nums[], size_t size, int key) {
  int start = 0;
  int end = size - 1;
  int answer = size;
  while (start <= end) {
    int mid = (start + end) / 2;
    if (nums[mid] >= key) {
      answer = mid;
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return answer;
}

int LowerBound(int nums[], size_t size, int key) {
  int start = 0;
  int end = size - 1;
  int answer = 0;
  while (start <= end) {
    int mid = (start + end) / 2;
    if (nums[mid] <= key) {
      answer = mid;
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return answer;
}

int Sqrt(int x) {
  if (x == 0) {
    return 0;
  }
  int start = 1;
  int end = x / 2;
  int answer = 1;
  while (start <= end) {
    int mid = (start + end) / 2;
    if (mid * mid == x) {
      return mid; 
    } else if (mid * mid < x) {
      start = mid + 1;
      answer = mid;
    } else {
      end = mid - 1;
    }
  }
  return answer;
}
