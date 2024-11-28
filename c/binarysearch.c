#include "stdio.h"

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

