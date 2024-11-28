#include <malloc.h>
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

void PrintArray(int nums[], size_t size) {
  for (int i = 0; i < size; i++) {
    printf("%d ", nums[i]);
  }
  printf("\n");
}

void SlideWindow(int nums[], size_t size, int new) {
  for (int i = 1; i < size; i++) {
    nums[i - 1] = nums[i];
  }
  nums[size - 1] = new;
}

void ViewWindowK(int nums[], size_t size,int k) {
  if (k <= 0 || k > size) {
    return;
  }
  int sum = 0;
  int* window = (int*) malloc(sizeof(int) * k);
  for (int i = 0; i < k; i++) {
    window[i] = nums[i];
  }
  PrintArray(window, k);
  for (int i = k; i < size; i++) {
    SlideWindow(window, k, nums[i]); 
    PrintArray(window, k);
  }
}

float* WindowMean(int nums[], size_t size, int k, int* returnSize) {
  *returnSize = size - k + 1;
  float* answer = (float*) malloc(sizeof(float) * (size - k + 1));
  int left = 0;
  int right = 0;
  int wSum = 0;
  while (right < k) {
    wSum += nums[right];
    right++;
  }
  answer[0] = (float) wSum / k;
  int index = 1;
  while (right < size) {
    wSum -= nums[left];
    left++;
    right++;
    wSum += nums[right];
    answer[index] = (float) wSum / k;
    index++;
  }
  return answer;
}

int MaxSubArraySubI(int nums[], size_t size) {
  int sum = 0;
  int answer = 0;
  for (int i = 0; i < size; i++) {
    sum = maxInt(nums[i], sum + nums[i]);
    answer = maxInt(answer, sum);
  }
  return answer;
}

int* MaxSubArraySumII(int nums[], size_t size, int* returnSize) {
  int sum = 0;
  int max = 0;
  int start = 0;
  int end = 0;
  int* answer = (int*) malloc(sizeof(int) * 2);
  *returnSize = 2;
  for (int i = 0; i < size; i++) {
    if (sum == 0) {
      start = i;
    }
    sum += nums[i];
    if (sum > max) {
      max = sum;
      end = i;
    }
    if (sum < 0) {
      sum = 0;
    }
  }
  answer[0] = start;
  answer[1] = end;
  return answer;
}

int LongestSubArrayWithSumI(int nums[], size_t size, int k) {
  int i = 0;
  int answer = 0;
  int sum = 0;
  for (int j = 0; j < size; j++) {
    sum += nums[j];
    if (sum == k) {
      answer = maxInt(answer, j - i + 1);
      sum -= nums[i];
      i++;
    }
    while (sum >= k && i <= j) {
      sum -= nums[i];
      i++;
    }
  }
  return answer;
}

int* LongestSubArrayWithSumII(int nums[], size_t size, int k, int* returnSize) {
  int sum = 0;
  int start = 0;
  int end = 0;
  int* answer = (int*) malloc(*returnSize);
  *returnSize = 2;
  for (int i = 0; i < size; i++) {
    sum += nums[i];
    if (sum == k) {
      end = i;
    }
    while (sum > k) {
      sum -= nums[start];
      start++;
    }
  }
  answer[0] = start;
  answer[1] = end;
  return answer;
}

int main() {
  int nums[8] = {1,2,3,4,5,6,7,8};
  size_t size = 8;
  int returnSize;
  ViewWindowK(nums, size, 3);
  float* answer = WindowMean(nums, size, 3, &returnSize);
  for (int i = 0; i < returnSize; i++) {
    printf("%f ", answer[i]);
  }
  return 0;
}
