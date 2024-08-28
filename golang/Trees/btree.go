package trees

import (
	"math"
)

type TreeNode struct {
	Left   *TreeNode
	Right  *TreeNode
	Parent *TreeNode
	Value  int
}

func BreadthFirstTraversalI(root *TreeNode) []int {
	var elements []int
	var queue []*TreeNode
	queue = append(queue, root)
	for len(queue) != 0 {
		var node *TreeNode = queue[0]
		queue = queue[1:]
		elements = append(elements, node.Value)
		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}
	return elements
}

func BreadthFirstTraversalII(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	var elements [][]int
	var queue []*TreeNode
	queue = append(queue, root)
	for len(queue) != 0 {
		var base int = len(queue)
		var level = []int{}
		for i := 0; i < base; i++ {
			var node *TreeNode = queue[0]
			queue = queue[1:]
			level = append(level, node.Value)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		elements = append(elements, level)
	}
	return elements
}

func BreadthFirstTraversalIII(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	var elements [][]int
	var queue []*TreeNode
	queue = append(queue, root)
	for len(queue) != 0 {
		var base int = len(queue)
		var level = []int{}
		for i := 0; i < base; i++ {
			var node *TreeNode = queue[0]
			queue = queue[1:]
			level = append(level, node.Value)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		elements = append([][]int{level}, elements...)
	}
  return elements
}

func DepthFirstTraversal(root *TreeNode) []int {
	var elements []int
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) != 0 {
		var node *TreeNode = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		elements = append(elements, node.Value)
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	return elements
}

func BreadthFirstSearch(root *TreeNode, key int) bool {
	var queue []*TreeNode
	queue = append(queue, root)
	for len(queue) != 0 {
		var node *TreeNode = queue[0]
		queue = queue[1:]
		if node.Value == key {
			return true
		}
		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}
	return false
}

func DepthFirstSearch(root *TreeNode, key int) bool {
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) != 0 {
		var node *TreeNode = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if node.Value == key {
			return true
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	return false
}

func DepthFirstSearchRecusive(root *TreeNode, key int) bool {
	if root == nil {
		return false
	}
	if root.Value == key {
		return true
	}
	return DepthFirstSearchRecusive(root.Left, key) || DepthFirstSearchRecusive(root.Right, key)
}

func SearchBST(root *TreeNode, val int) *TreeNode {
  if root == nil {
    return nil
  }
  if root.Value == val {
    return root
  } else if root.Value > val {
    return SearchBST(root.Left, val)
  } else {
    return SearchBST(root.Right, val)
  }
}

func TreeMinimumDFS(root *TreeNode) int {
	var minimum int = math.MaxInt
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) != 0 {
		var node *TreeNode = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if node.Value < minimum {
			minimum = node.Value
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	return minimum
}

func TreeMinimumBFS(root *TreeNode) int {
	var minimum int = math.MaxInt
  var queue []*TreeNode
  queue = append(queue, root)
  for len(queue) != 0 {
    var node *TreeNode = queue[0]
    queue = queue[1:]
    if node.Value < minimum {
      minimum = node.Value
    }
    if node.Left != nil {
      queue = append(queue, node.Left)
    }
    if node.Right != nil {
      queue = append(queue, node.Right)
    }
  }
  return minimum
}

func TreeMaximumDFS(root *TreeNode) int {
	var maximum int = math.MinInt
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) != 0 {
		var node *TreeNode = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if node.Value > maximum {
			maximum = node.Value
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	return maximum
}

func TreeMaximumBFS(root *TreeNode) int {
	var maximum int = math.MaxInt
  var queue []*TreeNode
  queue = append(queue, root)
  for len(queue) != 0 {
    var node *TreeNode = queue[0]
    queue = queue[1:]
    if node.Value > maximum {
      maximum = node.Value
    }
    if node.Left != nil {
      queue = append(queue, node.Left)
    }
    if node.Right != nil {
      queue = append(queue, node.Right)
    }
  }
  return maximum
}

func TreeSumDFS(root *TreeNode) int {
	var sum int = 0
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) != 0 {
		var node *TreeNode = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		sum += node.Value
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	return sum
}

func TreeSumBFS(root *TreeNode) int {
	var sum int = 0
	var queue []*TreeNode
	queue = append(queue, root)
	for len(queue) != 0 {
		var node *TreeNode = queue[0]
		queue = queue[1:]
		sum += node.Value
		if node.Left != nil {
			queue = append(queue, node.Left)
		}
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
	}
	return sum
}

func TreeSumRecursive(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return root.Value + TreeSumRecursive(root.Left) + TreeSumRecursive(root.Right)
}

func preorderTraversal(root *TreeNode, elements []int) []int {
	elements = append(elements, root.Value)
	if root.Left != nil {
		elements = preorderTraversal(root.Left, elements)
	}
	if root.Right != nil {
		elements = preorderTraversal(root.Right, elements)
	}
	return elements
}

func inorderTraversal(root *TreeNode, elements []int) []int {
	if root.Left != nil {
		elements = inorderTraversal(root.Left, elements)
	}
	elements = append(elements, root.Value)
	if root.Right != nil {
		elements = inorderTraversal(root.Right, elements)
	}
	return elements
}

func postorderTraversal(root *TreeNode, elements []int) []int {
	if root.Left != nil {
		elements = postorderTraversal(root.Left, elements)
	}
	if root.Right != nil {
		elements = postorderTraversal(root.Right, elements)
	}
	elements = append(elements, root.Value)
	return elements
}

func PreorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var elements []int
	return preorderTraversal(root, elements)
}

func InorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var elements []int
	return inorderTraversal(root, elements)
}

func PostorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var elements []int
	return postorderTraversal(root, elements)
}

func BSTInsert(root *TreeNode, val int) {
  if root == nil {
    root =  &TreeNode{Value: val}
  }
  if root.Value >= val {
    if root.Left != nil {
      BSTInsert(root.Left, val)
    } else {
      root.Left = &TreeNode{Value: val}
    }
  } else {
    if root.Right != nil {
      BSTInsert(root, val)
    } else {
      root.Right = &TreeNode{Value: val}
    }
  }
}

func TreeDepthBFS(root *TreeNode) int {
  var depth int = 0
  var queue []*TreeNode
  queue = append(queue, root)
  for len(queue) != 0 {
    for range queue {
      var node *TreeNode = queue[0]
      queue = queue[1:]
      if node.Left != nil {
        queue = append(queue, node.Left)
      }
      if node.Right != nil {
        queue = append(queue, node.Right)
      }
    }
    depth++
  }
  return depth
}

func TreeDepthDFSRecursive(root *TreeNode) int {
  var dfs func(root *TreeNode, depth float64) float64
  dfs = func(root *TreeNode, depth float64) float64 {
    if root == nil {
      return depth
    } else {
      return math.Max(dfs(root.Left, depth + 1), dfs(root.Right, depth + 1))
    }
  } 
  return int(dfs(root, 0))
}

func InvertTree(root *TreeNode) *TreeNode {
  if root == nil {
    return nil
  }
  var queue []*TreeNode
  queue = append(queue, root)
  for len(queue) != 0 {
    var node *TreeNode = queue[0]
    queue = queue[1:]
    if node.Left != nil {
      queue = append(queue, node.Left)
    }
    if node.Right != nil {
      queue = append(queue, node.Right)
    }
    node.Left, node.Right = node.Right, node.Left
  }
  return root
}

func SameTree(p, q *TreeNode) bool {
  if p == nil && q == nil {
    return true
  } 
  if p == nil || q == nil {
    return false
  }
  if p.Value == q.Value {
    return SameTree(p.Left, q.Left) && SameTree(p.Right, q.Right)
  }
  return false
}

func CountNodesBFS(root *TreeNode) int {
  if root == nil {
    return 0
  }
  var count int = 0
  var queue []*TreeNode
  queue = append(queue, root)
  for len(queue) != 0 {
    var node *TreeNode = queue[0]
    queue = queue[1:]
    count++
    if node.Left != nil {
      queue = append(queue, node.Left)
    }
    if node.Right != nil {
      queue = append(queue, node.Right)
    }
  }
  return count
}

func CountNodesDFS(root *TreeNode) int {
  if root == nil {
    return 0
  }
  var count int = 0
  var stack []*TreeNode
  stack = append(stack, root)
  for len(stack) != 0 {
    var node *TreeNode = stack[len(stack)-1]
    stack = stack[:len(stack)-1]
    count++
    if node.Left != nil {
      stack = append(stack, node.Left)
    }
    if node.Right != nil {
      stack = append(stack, node.Right)
    }
  }
  return count
}

func CountNodesRecursive(root *TreeNode) int {
  if root == nil {
    return 0
  }
  return 1 + CountNodesRecursive(root.Left) + CountNodesRecursive(root.Right)
}
