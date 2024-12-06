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

int* WindowSum(int nums[], size_t size, int k, int* returnSize) {
  int* answer = (int*) malloc(sizeof(int));
  int left = 0;
  int right = k - 1;
  int wSum = 0;
  for (int i = 0; i < k; i++) {
    wSum += nums[i];
  }
  answer[0] = wSum;
  int index = 1;
  while (right < size) {
    wSum -= nums[left];
    left++;
    right++;
    wSum += nums[right];
    answer = realloc(answer, sizeof(int) * index + 1);
    answer[index] = wSum;
    index++;
  }
  *returnSize = index - 1;
  return answer;
}

float* WindowMean(int nums[], size_t size, int k, int* returnSize) {
  float* answer = (float*) malloc(sizeof(float));
  int left = 0;
  int right = k - 1;
  int wSum = 0;
  for (int i = 0; i < k; i++) {
    wSum += nums[i];
  }
  answer[0] = (float) wSum / k;
  int index = 1;
  while (right < size) {
    wSum -= nums[left];
    left++;
    right++;
    wSum += nums[right];
    answer = realloc(answer, sizeof(float) * index + 1);
    answer[index] = (float) wSum / k;
    index++;
  }
  *returnSize = index - 1;
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

int MaxWindowSum(int nums[], size_t size, int k) {
  int sum = 0;
  int left = 0;
  int right = k - 1;
  for (int i = 0; i < k; i++) {
    sum += nums[i];
  }
  int answer = sum;
  while (right < size) {
    sum -= nums[left];
    left++;
    right++;
    sum += nums[right];
    answer = maxInt(answer, sum);
  }
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
    }
    while (sum > k && i < j) {
      sum -= nums[i];
      if (sum == k) {
        answer = maxInt(answer, j - i + 1);
      }
      i++;
    }
  }
  return answer;
}

int* LongestSubArrayWithSumII(int nums[], size_t size, int k, int* returnSize) {
  int i = 0;
  int sum = 0;
  *returnSize = 2;
  int* answer = (int*) malloc(sizeof(int) * 2);
  for (int j = 0; j < size; j++) {
    sum += nums[j];
    if (sum == k) {
      answer[0] = i;
      answer[1] = j;
      sum -= nums[i];
      i++;
    }
    while (sum > k && i < j) {
      sum -= nums[i];
      if (sum == k) {
        answer[0] = i;
        answer[1] = j;
      }
      i++;
    }
  }
  return answer;
}

int SubArraysWithSumPositives(int nums[], size_t size, int k) {
  int sum = 0;
  int answer = 0;
  int j = 0;
  for (int i = 0; i < size; i++) {
    sum += nums[i];
    if (sum == k) {
      answer++;
      }
    while (sum > k && j < i) {
      sum -= nums[j];
      j++;
      if (sum == k) {
        answer++;
      }
    }
  }
  return answer;
}

int main() {
  int nums[8] = {1,2,3,4,5,6,7,8};
  size_t size = 8;
  int returnSize;
  int* answer = LongestSubArrayWithSumII(nums, size, 11, &returnSize);
  printf("%d %d\n", answer[0], answer[1]);
  printf("%d\n", LongestSubArrayWithSumI(nums, size, 11));
  return 0;
}
