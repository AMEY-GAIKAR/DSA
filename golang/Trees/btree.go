package trees

type TreeNode struct {
  Left *TreeNode
  Right *TreeNode
  Parent *TreeNode
  Value int
}

func BFS(root *TreeNode) [][]int {
  var elements [][]int 
  var queue []int
}
