#include <malloc.h>

struct ListNode {
  int val;
  struct ListNode* next;
};

struct ListNode* RemoveElements(struct ListNode* head, int key) {
  if (head == NULL) {
    return NULL;
  }
  struct ListNode* current = head;
  struct ListNode* prev;
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
