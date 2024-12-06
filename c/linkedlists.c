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
