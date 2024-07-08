const BinarySearchRecursive = (array, value, start, end) => {
  if (end >= start) {
    let mid = Math.floor((start + end) / 2)
    if (array[mid] == value) {
    return mid
  }
    else if (value > array[mid]) {
      start = mid + 1
      return BinarySearchRecursive(array, value, start, end)
    }
    else {
      end = mid - 1
      return BinarySearchRecursive(array, value, start, end)
    }
  }
  return -1
}

const BinarySearch = (array, value) => {
  let start = 0
  let end = array.length
  while (end >= start) {
    let mid = Math.floor((start + end) / 2)
    if (array[mid] == value) {
      return mid
    }
    else if (value > array[mid]) {
      start = mid + 1 
    }
    else {
      end = mid - 1
    }
  }
  return -1
}

const LowerBound = (array, target) => {
  let start = 0 
  let end = array.length
  let position = 0
  while (end >= start) {
    let mid = Math.floor((start + end) / 2)
    if (target <= array[mid]) {
      position = mid
      end = mid - 1
    } 
    else {
      start = mid + 1
    }
  }
  return position
} 

const UpperBound = (array, target) => {
  let start = 0 
  let end = array.length
  let position = array.length
  while (end >= start) {
    let mid = Math.floor((start + end) / 2)
    if (target < array[mid]) {
      position = mid
      end = mid - 1
    } 
    else {
      start = mid + 1
    }
  }
  return position
} 
