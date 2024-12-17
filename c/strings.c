#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char FindDuplicate(char* s) {
  int c = 0;
  while (s[c] != '\0') {
    for (int i = c + 1; i < strlen(s); i++) {
      if (s[c] ==  s[i]) {
        return s[c];
      }
    }
    c++;
  }
  return '\0';
}

bool IsRepeated(char* s) {
  for (int i = 0; i < strlen(s); i++) {
    for (int j = i + 1; j < strlen(s); j++) {
      if (s[i] == s[j]) {
        return true;;
      }
    }
  }
  return false;
}

bool IsPalindrome(char* s) {
  int i = 0;
  int j = strlen(s) - 1;
  while (i < j) {
    if (isalpha(s[i]) == 0) {
      i++;
    } else if (isalpha(s[j]) == 0) {
      j--;
    } else {
      if (tolower(s[i]) != tolower(s[j])) {
       return false;
      }
      i++;
      j--;
    }
  }
  return true;
}

void ReverseString(char s[]) {
  int i = 0;
  int j = strlen(s) - 1;
  while (i < j) {
    printf("%c %c\n", s[i], s[j]);
    int temp = s[i];
    s[i] = s[j];
    s[j] = temp;
    i++;
    j--;
  }
}

int main() {

  char s[] = "Nan";
  // int result = IsPalindrome(s);
  // printf("%d\n", result);
  ReverseString(s);
  printf("%s\n", s);
  return 0;
}
