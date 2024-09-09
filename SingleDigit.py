'''Given a number N, your task is to make N a single digit number by performing the following operations:
1. if N is odd make it floor(N/2)
2. if N is even make it floor(N-2)/2
3. if N is single digit return it as it is'''
import math
def single_digit(n):
    if n%10 == n:
        return n
    elif n%2 != 0:
        n = math.floor(n/2)
        return single_digit(n)
    else:
        n = math.floor((n-2)/2)
        return single_digit(n)
def main():
    n = int(input())
    res = single_digit(n)
    print(res)
if __name__ == "__main__":
    main()
    
