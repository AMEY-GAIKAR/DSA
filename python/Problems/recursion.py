def pow(x: float, n: int) -> float:
    if n > 0:
        return x*pow(x, n-1)
    elif n <= -1:
        return 1/x*pow(x, n+1) 
    return 1

if __name__ == "__main__":
    print(pow(0.00001, 2147483647))
