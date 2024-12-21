package linkedlists

type ListNode struct {
    Val int
    Next *ListNode
}

type MyLinkedList struct {
    Head *ListNode
    Length int
}

func Constructor() MyLinkedList {
    return MyLinkedList{}
}

func (this *MyLinkedList) Get(index int) int {
    if index < 0 || index >= this.Length {
        return -1
    }
    var current *ListNode = this.Head
    for i:=0; i<index; i++{
        current = current.Next
    }
    return current.Val
}

func (this *MyLinkedList) AddAtHead(val int)  {
    if this.Head == nil {
        this.Head = &ListNode{Val: val}
        this.Length++
        return
    }
    var second *ListNode = this.Head
    this.Head = &ListNode{Val: val, Next: second}
    this.Length++
    return
}

func (this *MyLinkedList) AddAtTail(val int)  {
    if this.Head == nil {
        this.Head = &ListNode{Val: val}
        this.Length++
        return 
    }
    var current *ListNode = this.Head
    for current.Next != nil {
        current = current.Next
    }
    current.Next = &ListNode{Val: val}
    this.Length++
    return
}

func (this *MyLinkedList) AddAtIndex(index int, val int)  {
    if index < 0 || index > this.Length {
        return
    }
    if index == 0 {
        this.AddAtHead(val)
        return
    }
    var current *ListNode = this.Head
    for i:=0; i<index-1; i++ {
        current = current.Next
    }
    n := &ListNode{Val: val,Next: current.Next}
    current.Next = n
    this.Length++
}

func (this *MyLinkedList) DeleteAtIndex(index int)  {
    if index < 0 || index >= this.Length {
        return
    }
    if index == 0 {
        this.Head = this.Head.Next
        this.Length--
        return
    }
    var current *ListNode = this.Head
    for i:=0; i<index-1; i++ {
        current = current.Next
    }
    current.Next = current.Next.Next
    this.Length--
}

func TraverseList(head *ListNode) []int {
  var elements = []int{}  
  var current *ListNode = head
  for current != nil {
    elements = append(elements, current.Val)
    current = current.Next
  }
  return elements
}

func RemoveElements(head *ListNode, val int) *ListNode {
	current := head
	var prev *ListNode
	for current != nil {
	if current.Val == val {
		if prev == nil {
			head = current.Next
		} else {
			prev.Next = current.Next
		}
    current = current.Next
		} else {
      prev = current
      current = current.Next
    }
  }
  return head
}

func MiddleNodeI(head *ListNode) *ListNode {
  var fast *ListNode = head
  var slow *ListNode = head
  for fast != nil && fast.Next != nil {
    fast = fast.Next.Next
    slow = slow.Next
  }
  return slow
}

func MiddleNodeII(head *ListNode) *ListNode {
  var middle *ListNode = head
  var current *ListNode = head
  var i int = 0
  for current.Next != nil {
    i++
    current = current.Next
    if i % 2 == 0 {
      middle = middle.Next
    }
  }
  if i % 2 == 0 {
    return middle
  }
  return middle.Next
}

func ReverseList(head *ListNode) *ListNode {
  if head == nil {
    return head
  }
  var current *ListNode = head
  var prev *ListNode
  for current.Next != nil {
    var temp *ListNode = current.Next
    current.Next = prev
    prev = current
    current = temp
  }
  current.Next = prev
  return current
}

func HasCycleI(head *ListNode) bool {
  var fast *ListNode = head
  var slow *ListNode = head
  for fast != nil && fast.Next.Next != nil {
    fast = fast.Next.Next
    slow = slow.Next
    if fast == slow {
      return true
    }
  }
  return false
}

func HasCycleII(head *ListNode) bool {
  unique := make(map[*ListNode]bool)
  var current *ListNode = head
  for current != nil {
    if _, ok := unique[current]; ok {
      return true 
    } else {
      unique[current] = true
      current = current.Next
    }
  }
  return false
}

func DetectCycleI(head *ListNode) *ListNode {
  var fast *ListNode = head
  var slow *ListNode = head
  for fast != nil && fast.Next != nil {
    fast = fast.Next.Next
    slow = slow.Next
    if fast == slow {
      slow = head
      for slow != fast {
        slow = slow.Next
        fast = fast.Next
      }
      return slow
    }
  }
  return nil
}

func DetectCycleII(head *ListNode) *ListNode {
  unique := make(map[*ListNode]bool)
  var current *ListNode = head
  for current != nil {
    if _, ok := unique[current]; ok {
      return current
    }
    unique[current] = true
    current = current.Next
  }
  return nil
}

func DeleteMiddle(head *ListNode) *ListNode {
  if head.Next == nil {
    return nil
  }
  var fast *ListNode = head
  var slow *ListNode = head
  var prev *ListNode
  for fast != nil && fast.Next != nil {
    fast = fast.Next.Next
    prev = slow
    slow = slow.Next
  }
  prev.Next = slow.Next
  return head
}

func RemoveNthNode(head *ListNode, n int) *ListNode {
  var fast *ListNode = head
  var slow *ListNode = head
  for i := 0; i < n; i++ {
    fast = fast.Next
  }
  if fast == nil {
    return head.Next
  }
  for fast.Next != nil {
    fast = fast.Next
    slow = slow.Next
  }
  slow.Next = slow.Next.Next
  return head
}

func ArrayToList(nums []int) *ListNode {
  if len(nums) == 0 {
    return nil
  }
  var head *ListNode = &ListNode{Val: nums[0]}
  var current *ListNode = head
  for i := 1; i <= len(nums); i++ {
    var node *ListNode = &ListNode{Val: nums[i]}
    current.Next =  node
    current = node
  }
  return head
}

func GetIntersectionNode(h1, h2 *ListNode) *ListNode {
  check := make(map[*ListNode]bool)
  var current *ListNode = h1
  for current != nil {
    check[current] = true
    current = current.Next
  }
  current = h2
  for current != nil {
    if _, exist := check[current]; exist {
      return current
    }
    current = current.Next
  }
  return nil
}

func PalindromeList(head *ListNode) bool {
  var elements = []int{}
  var current *ListNode = head
  for current != nil {
    elements = append(elements, current.Val)
    current = current.Next
  }
  var i int = 0
  var j int = len(elements) - 1
  for i < j {
    if elements[i] != elements[j] {
      return false
    }
    i++
    j--
  }
  return true
}

func MergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
  var result *ListNode = &ListNode{0, nil}
  var r *ListNode = result
  var p1 *ListNode = list1
  var p2 *ListNode = list2
  for p1 != nil && p2 != nil {
    if p1.Val < p2.Val {
      r.Next = p1
      p1 = p1.Next
    } else {
      r.Next = p2
      p2 = p2.Next
    }
    r = r.Next
  }
  if p1 != nil {
    r.Next = p1
  } else {
    r.Next = p2
  }
  return result.Next
}

func ReorderList(head *ListNode)  {
  l1 := head
  l2 := ReverseList(MiddleNodeI(head))
  for l2.Next != nil {
    l1.Next, l1 = l2, l1.Next
    l2.Next, l2 = l1, l2.Next
  }
}

func GetDecimalValue(head *ListNode) int {
  var elements = []int{}
  var current *ListNode = head
  var base int = 1
  var answer int = 0
  for current != nil {
    elements = append(elements, current.Val)
    current = current.Next
  }
  for i := len(elements) - 1; i > -1; i-- {
    answer += base * elements[i]
    base *= 2
  }
  return answer
} 

func AddTwoNumbers(l1, l2 *ListNode) *ListNode {
  var sum, carry int = 0, 0
  var result *ListNode = &ListNode{0, nil}
  var p1, p2, r *ListNode = l1, l2, result
  for p1 != nil && p2 != nil {
    sum = p1.Val + p2.Val + carry
    carry = sum / 10
    new := ListNode{sum % 10, nil}
    r.Next = &new
    r = &new
    p1 = p1.Next
    p2 = p2.Next
  }
  if p1 != nil && p2 != nil && carry == 1 {
    r.Next = &ListNode{1, nil}
  }
  if p1 != nil {
    for p1 != nil {
      sum = p1.Val + carry
      new := ListNode{sum % 10, nil}
      carry = sum / 10
      r.Next = &new
      r = &new
      p1 = p1.Next
    }
    if carry == 1 {
      r.Next = &ListNode{1, nil}
    }
  } else if p2 != nil {
    for p2 != nil {
      sum = p2.Val + carry
      new := ListNode{sum % 10, nil}
      carry = sum / 10
      r.Next = &new
      r = &new
      p2 = p2.Next
    }
    if carry == 1 {
      r.Next = &ListNode{1, nil}
    }
  }
  return result.Next
}
