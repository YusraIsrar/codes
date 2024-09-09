def sum_of_odd(n, arr):
    return sum(x for x in arr if x % 2 != 0)
def main():
    n = int(input())
    arr = []
    for i in range(n):
        ele = int(input())
        arr.append(ele)
    res = sum_of_odd(n, arr)
    print(res)
if __name__ == "__main__":
    main()

