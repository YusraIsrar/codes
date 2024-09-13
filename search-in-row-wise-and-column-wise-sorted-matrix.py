def search_matrix(mat, n, target):
    i = 0
    j = n-1
    while(i<n and j>= 0):
        if mat[i][j] == target:
            print(f"{i}, {j}")
            return 
        elif mat[i][j]>target:
            j -=1 
        else:
            i+=1 
    print("Element not found")
    return 0
if __name__ == "__main__":
    n = int(input())
    mat = [[int(input()) for x in range (n)] for y in range(n)]
    target = int(input())
    search_matrix(mat, n, target)
