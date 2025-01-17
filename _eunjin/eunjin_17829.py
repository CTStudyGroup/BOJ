N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def get2ndMax(matrix):
    arr = []
    for row in matrix:
        for elem in row:
            arr.append(elem)
    arr.sort()
    return arr[len(arr)-2]


def recursion(matrix, n):
    # base case
    if n == 2:
        print(get2ndMax(matrix))
        return

    # recursive case
    m = [[0]*(n//2) for _ in range(n//2)]
    for y in range(0, n, 2):
        for x in range(0, n, 2):
            temp_m = [[matrix[y][x], matrix[y][x+1]], [matrix[y+1][x], matrix[y+1][x+1]]]
            m[y//2][x//2] = get2ndMax(temp_m)
    recursion(m, n//2)


recursion(matrix, N)
