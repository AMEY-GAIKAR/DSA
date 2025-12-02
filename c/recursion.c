#include <stdio.h>

void PrintN(char *str, int n) {
  if (n == 1) {
    return;
  } else {
    printf("%s\n", str);
    PrintN(str, n - 1);
  }
}

void PrintNumbersI(int n) {
  if (n == 0) {
    return;
  } else {
    printf("%d\n", n);
    PrintNumbersI(n - 1);
  }
}

void PrintNumbersII(int n, int c) {
  if (c == n + 1) {
    return;
  } else {
    printf("%d\n", c);
    PrintNumbersII(n, c + 1);
  }
}

int Addition(int n) {
  if (n == 0) {
    return 0;
  } else {
    return n + Addition(n - 1);
  }
}

long long Factorial(int n) {
  if (n == 0) {
    return 1;
  } else {
    return n * Factorial(n - 1);
  }
}

int BinarySearch(int nums[], size_t size, int target, int start, int end) {
  if (start > end) {
    return -1;
  } else {
    int mid = (start + end) / 2;
    if (nums[mid] == target) {
      return mid;
    } else if (nums[mid] < target) {
      return BinarySearch(nums, size, target, mid + 1, end);
    } else {
      return BinarySearch(nums, size, target, start, mid - 1);
    }
  }
}
