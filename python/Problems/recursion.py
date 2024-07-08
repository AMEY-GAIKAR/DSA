def pow(x: float, n: int) -> float:
    """
    Set base condition as:
    if n is 0 return 1 
    else if n is positive reduce n by 1 and call the function again.
    else if n is negative increase n by 1 and and make recursive call.
        
    """
    if n > 0:
        return x*pow(x, n-1)
    elif n <= -1:
        return 1/x*pow(x, n+1) 
    return 1

if __name__ == "__main__":
    print(pow(0.00001, 2147483647))
