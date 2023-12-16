//     a
//    / \
//   b   c
//  /\   /\
// d  e f  g

//     10
//    / \
//   8   13
//  /\   /\
// 7  9 12  15

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const A = new Node(10);
const B = new Node(8);
const C = new Node(13);
const D = new Node(7);
const E = new Node(9);
const F = new Node(12);
const G = new Node(15);

A.left = B;
A.right = C;
B.left = D;
B.right = E;
C.left = F;
C.right = G;

const depthFirstTraversal = (node) => {
  if (node === null) return []; 

  const stack = [];
  const nodes = [];
  
  stack.push(node);

  while (stack.length != 0) {
    const current = stack.pop();
    nodes.push(current.value);

    if (current.right) stack.push(current.right);
    if (current.left) stack.push(current.left);
  }

  return nodes;
};

const breadthFirstTraversal = (node) => {
  if (node === null) return [];

  const queue = [];
  const nodes = [];

  queue.push(node);

  while(queue.length != 0) {
    const current = queue.shift();
    nodes.push(current.value);

    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);
  }

  return nodes;
};

const breadthFirstSearch = (node, value) => {

  if (node === null) return false;

  const queue = [];

  queue.push(node);

  while(queue.length != 0) {

    const current = queue.shift();
   
    if (current.value === value) {
      return true;
    } else {
    
    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);
    }
  }
  return false;
};

const depthFirstSearch = (node, value) => {
  if (node === null) return false; 

  const stack = [];
  
  stack.push(node);

  while (stack.length != 0) {
    
    const current = stack.pop();
    
    if (current.value === value) {
      return true;
    } else {
    
    if (current.right) stack.push(current.right);
    if (current.left) stack.push(current.left);    
    }
  }
  return false;
};

const depthFirstSearchRecusive = (node, value) => {
  if (node === null) return false;
  if (node.value === value) return true;
  return depthFirstSearchRecusive(node.left, value) || depthFirstSearchRecusive(node.right, value);
};

const treeSumRecursive = (node) => {
  if (node === null) return 0;
  
  return node.value + treeSumRecursive(node.left) + treeSumRecursive(node.right);
};

const treeSumBFS = (node) => {
  if (node === null) return 0;

  const queue = [];
  let sum = 0;
  
  queue.push(node);

  while (queue.length != 0) {
    const current = queue.shift();
    sum += current.value;

    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);
  }
  return sum;
};

const treeSumDFS = (node) => {
  if (node === null) return 0;

  const stack = []
  let sum = 0;

  stack.push(node);

  while (stack.length != 0) {
    const current = stack.pop();
    sum += current.value;

    if (current.right) stack.push(current.right);
    if (current.left) stack.push(current.left);
  }
  return sum;
};


