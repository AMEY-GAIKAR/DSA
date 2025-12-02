#include <malloc.h>
#include <math.h>
#include <stdbool.h>

int GCD(int a, int b) {
  int gcd = 1;
  int smaller = 0;
  if (a < b) {
    smaller = a;
  } else {
    smaller = b;
  }
  for (int i = 1; i <= smaller; i++) {
    if ((a % i == 0) && (b % i == 0)) {
      gcd = i;
    }
  }
  return gcd;
}

bool IsPrime(int n) {
  if (n == 2) {
    return true;
  }
  if (n <= 1 || n % 2 == 0) {
    return false;
  }
  for (int i = 3; i <= sqrt(n); i += 2) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

long long NthPrime(int n) {
  long long prime = 2;
  int count = 1;
  int i = 3;
  while (count != n) {
    if (IsPrime(i) == true) {
      prime = i;
      count++;
    }
    i += 2;
  }
  return prime;
}

int *PrimeFactors(int n, int *returSize) {
  int buffSize = 8;
  int *buffer = (int *)malloc(sizeof(int) * buffSize);
  int idx = 0;
  for (int i = 2; i <= n; i++) {
    if (n % i == 0) {
      if (IsPrime(i) == true) {
        buffer[idx++] = i;
        if (idx <= buffSize) {
          buffer = realloc(buffer, sizeof(int) * idx * 2);
        }
      }
    }
  }
  buffer = realloc(buffer, sizeof(int) * idx);
  *returSize = idx;
  return buffer;
}

bool IsPalindrome(int x) {
  if (x < 0 || (x % 10 == 0 && x != 0)) {
    return false;
  }
  int reverse = 0;
  while (x > reverse) {
    reverse = reverse * 10 + x % 10;
    x /= 10;
  }
  return x == reverse || x == reverse / 10;
}
