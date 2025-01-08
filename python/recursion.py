def recursionPrint(x: int) -> None:
    if x == 0:
        print("Base Case")
        return None
    print(f'{x}th case.')
    return recursionPrint(x-1)

def recursionCountDec(x: int) -> None:
    if x == 0:
        print(f'Case: {x}')
        return None
    print(f'Case: {x}')
    return recursionCountDec(x-1)

def recursionCountInc(x: int, n: int = 1) -> None:
    if n == x:
        print(f'Case: {x}')
        return None
    print(f'Case: {n}')
    return recursionCountInc(x,n+1)

def recursiveSumI(x: int, sum: int = 0) -> int:
    if x == 0:
        return sum
    return recursiveSumI(x-1, sum+x)

def recursiveSumII(x: int) -> int:
    if x == 0:
        return 0
    return x + recursiveSumII(x-1)

def recursiveFactorialI(x: int, factorial: int = 1) -> int:
    if x == 1:
        return factorial
    return recursiveFactorialI(x-1, factorial*x)

def recursiveFactorialII(x: int) -> int:
    if x == 0:
        return 1
    return x * recursiveFactorialII(x-1)

def recursiveFibonacci(n: int) -> int:
    if n <= 1:
        return n
    last: int = recursiveFibonacci(n-1)
    second_last: int = recursiveFibonacci(n-2)

    return last + second_last

def pow(x: float, n: int) -> float:
    if n > 0:
        return x*pow(x, n-1)
    elif n <= -1:
        return 1/x*pow(x, n+1) 
    return 1
