def rotate(arr, k):
    arr = arr[::-1]
    arr_rot = arr[:k][::-1]+arr[k:][::-1]
    return(arr_rot)
def main():
    k = int(input())
    arr = list(map(int, input().split(',')))
    res = rotate(arr, k)
    print(res)
if __name__ == "__main__":
    main()
    
