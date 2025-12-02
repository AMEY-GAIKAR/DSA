#include <ctype.h>
#include <malloc.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

char FindDuplicate(char *s) {
  int c = 0;
  while (s[c] != '\0') {
    for (int i = c + 1; i < strlen(s); i++) {
      if (s[c] == s[i]) {
        return s[c];
      }
    }
    c++;
  }
  return '\0';
}

bool IsRepeated(char *s) {
  for (int i = 0; i < strlen(s); i++) {
    for (int j = i + 1; j < strlen(s); j++) {
      if (s[i] == s[j]) {
        return true;
        ;
      }
    }
  }
  return false;
}

bool IsPalindrome(char *s) {
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

bool canConstruct(char *ransomNote, char *magazine) {
  int map[26] = {0};
  while (*magazine) {
    map[*magazine - 'a']++;
    magazine++;
  }
  while (*ransomNote) {
    map[*ransomNote - 'a']--;
    ransomNote++;
  }
  for (int i = 0; i < 26; i++) {
    if (map[i] < 0) {
      return false;
    }
  }
  return true;
}

void ReverseString(char s[]) {
  int i = 0;
  int j = strlen(s) - 1;
  while (i < j) {
    int temp = s[i];
    s[i] = s[j];
    s[j] = temp;
    i++;
    j--;
  }
}

int *FindWordsContaining(char **words, int wordsSize, char x, int *returnSize) {
  int *answer = (int *)malloc(sizeof(int) * wordsSize);
  int index = 0;
  for (int i = 0; i < wordsSize; i++) {
    for (int j = 0; j < strlen(words[i]); j++) {
      if (words[i][j] == x) {
        answer[index++] = i;
        break;
      }
    }
  }
  *returnSize = index;
  int *result = (int *)realloc(answer, sizeof(int) * index);
  return result;
}

char **ReverseWords(char s[], int *len) {
  char **tokens = (char **)malloc((sizeof(char *) * 32));
  char *token;
  int position = 0;
  token = strtok(s, " ");
  while (token != NULL) {
    tokens[position++] = token;
    token = strtok(NULL, " ");
  }
  *len = position;
  int i = 0;
  int j = position - 1;
  while (i <= j) {
    char *temp = tokens[i];
    tokens[i] = tokens[j];
    tokens[j] = temp;
    i++;
    j--;
  }
  return tokens;
}
