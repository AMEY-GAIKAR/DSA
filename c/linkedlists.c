#include <stdbool.h>
#include <malloc.h>

struct ListNode {
  int val;
  struct ListNode* next;
};

void RemoveNode(struct ListNode* node) {
    node->val = node->next->val;
    node->next = node->next->next;
}

struct ListNode* RemoveElements(struct ListNode* head, int key) {
  if (head == NULL) {
    return NULL;
  }
  struct ListNode* current = head;
  struct ListNode* prev = NULL;
  while (current != NULL) {
    if (current->val == key) {
      if (prev == NULL) {
        head = current->next;
      } else {
        prev->next = current->next;
      }
      current = current->next;
    } else {
      prev = current;
      current = current->next;
    }
  }
  return head;
}

struct ListNode* MiddleNodeI(struct ListNode* head) {
  struct ListNode* fast = head;
  struct ListNode* slow = head;
  while (fast != NULL && fast->next != NULL) {
    fast = fast->next->next;
    slow = slow->next;
  }
  return slow;
}

struct ListNode* MiddleNodeII(struct ListNode* head) {
  struct ListNode* current = head;
  struct ListNode* middle = head;
  int i = 0;
  while (current->next != NULL) {
    current = current->next;
    i++;
    if (i % 2 == 0) {
      middle = middle->next;
    }
  }
  if (i % 2 == 0) {
    return middle;
  }
  return middle->next;
}

struct ListNode* ReverseList(struct ListNode* head) {
  if (head == NULL || head->next == NULL) {
    return head;
  }
  struct ListNode* current = head;
  struct ListNode* prev = NULL;
  while (current->next != NULL) {
    struct ListNode* temp = current->next;
    current->next = prev;
    prev = current;
    current = temp;
  }
  current->next = prev;
  return current;
}

bool HasCycle(struct ListNode* head) {
  struct ListNode* fast = head;
  struct ListNode* slow = head;
  while (fast != NULL && fast->next != NULL) {
    fast = fast->next->next;
    slow = slow->next;
    if (fast == slow) {
      return true;
    }
  }
  return false;
}

struct ListNode* DetectCycle(struct ListNode* head) {
  struct ListNode* fast = head;
  struct ListNode* slow = head;
  while (fast != NULL && fast->next != NULL) {
    fast = fast->next->next;
    slow = slow->next;
    if (fast == slow) {
      slow = head;
      while (slow != fast) {
        slow = slow->next;
        fast = fast->next;
      }
      return slow;
    }
  }
  return NULL;
}

struct ListNode* MergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
  struct ListNode* p1 = list1;
  struct ListNode* p2 = list2;
  struct ListNode* newHead = (struct ListNode*) malloc(sizeof(struct ListNode));
  newHead->val = 0;
  newHead->next = NULL;
  struct ListNode* ptr = newHead;
  while (p1 != NULL && p2 != NULL) {
    if (p1->val < p2->val) {
      ptr->next = p1;
      p1 = p1->next;
    } else {
      ptr->next = p2;
      p2 = p2->next;
    }
    ptr = ptr->next;
  }
  if (p1 != NULL) {
    ptr->next = p1;
  } else {
    ptr->next = p2;
  }
  return newHead->next;
}

struct ListNode* RemoveDuplicates(struct ListNode* head) {
  if (head == NULL) {
    return head;
  }
  struct ListNode* current = head;
  struct ListNode* prev = head;
  int currentVal = head->val;
  while (current != NULL) {
    if (current->val == currentVal) {
      prev->next = current->next;
      currentVal = current->val;
    } else {
      currentVal = current->val;
      prev = current;
    }
    current = current->next;
  }
  return head;
}

/*
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *p=headA,*q=headB;
    while (p!=q){
        p=(p==NULL) ? headB : p->next;
        q=(q==NULL) ? headA : q->next;
    }
    return p;
}
*/
struct ListNode* IntersectionOfLists(struct ListNode* headA, struct ListNode* headB) {
  struct ListNode* p1 = headA;
  struct ListNode* p2 = headB;
  while (p1 != NULL) {
    while (p2 != NULL && p1 != p2) {
      p2 = p2->next;
      if (p1 == p2) {
        return p1;
      }
    }
    p1 = p1->next;
    p1 = headB;
  }
  return NULL;
}

int GetDecimalValue(struct ListNode* head) {
  int decimal = 0;
  int buffSize = 8;
  int* binary = (int*) malloc(sizeof(int) * buffSize);
  int idx = 0;
  int power = 1;
  struct ListNode* current = head;
  while (current != NULL) {
    binary[idx++] = current->val;
    if (idx >= buffSize) {
      binary = realloc(binary, sizeof(int) * idx * 2);
    }
    current = current->next;
  }
  binary = realloc(binary, sizeof(int) * idx);
  for (int i = idx - 1; i > -1; i--) {
    decimal += binary[i] * power;
    power *= 2;
  }
  return decimal;
}

bool PalindromeList(struct ListNode* head) {
  int buffSize = 8;
  int* buffer = malloc(sizeof(int) * buffSize);
  int idx = 0;
  struct ListNode* current = head;
  while (current != NULL) {
    buffer[idx++] = current->val;
    if (idx >= buffSize) {
      buffer = realloc(buffer, sizeof(int) * idx * 2);
    }
    current = current->next;
  }
  buffer = realloc(buffer, sizeof(int) * idx);
  int i = 0;
  int j = idx - 1;
  while (i <= j) {
    if (buffer[i] != buffer[j]) {
      return false;
    }
    i++;
    j--;
  }
  return true;
}
