def one(A):
    N, M = len(A), len(A[0])
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        tmp[i] = A[N-i-1]
    return tmp

def two(A):
    N, M = len(A), len(A[0])
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        tmp[i] = A[i][::-1]
    return tmp

def three(A):
    N, M = len(A), len(A[0])
    tmp = [[0]*M for _ in range(N)]
    for j in range(M):
        for i in range(N):
            tmp[i][j] = A[N-i-1][j]
    return list(map(list, zip(*tmp)))

def four(A):
    N, M = len(A), len(A[0])
    tmp = [[0]*M for _ in range(N)]
    for j in range(M):
        for i in range(N):
            tmp[i][j] = A[i][M-j-1]
    return list(map(list, zip(*tmp)))

def five(A):
    N, M = len(A), len(A[0])
    tmp = [[0]*M for _ in range(N)]
    for i in range(N//2): # group 1 -> group 2
        for j in range(M//2, M):
            tmp[i][j] = A[i][j-M//2]

    for i in range(N//2, N): # group 2 -> group 3
        for j in range(M//2, M):
            tmp[i][j] = A[i-N//2][j]

    for i in range(N//2, N): # group 3 -> group 4
        for j in range(M//2):
            tmp[i][j] = A[i][j+(M//2)]
    
    for i in range(N//2): # group 4 -> group 1
        for j in range(M//2):
            tmp[i][j] = A[i+(N//2)][j]
    return tmp

def six(A):
    N, M = len(A), len(A[0])
    tmp = [[0]*M for _ in range(N)]
    for i in range(N//2): # group 4 <- group 1
        for j in range(M//2):
            tmp[i+(N//2)][j] = A[i][j]

    for i in range(N//2, N): # group 3 <- group 4
        for j in range(M//2):
            tmp[i][j+(M//2)] = A[i][j]

    for i in range(N//2, N): # group 2 <- group 3
        for j in range(M//2, M):
            tmp[i-N//2][j] = A[i][j]

    for i in range(N//2): # group 1 <- group 2
        for j in range(M//2, M):
            tmp[i][j-M//2] = A[i][j]
    return tmp

def printA(A):
    for i in range(len(A)):
        print(*A[i])

# Input
N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Calc = list(map(int, input().split()))
calc_func = {1: one, 2: two, 3: three, 4: four, 5: five, 6: six}
for c in Calc:
    A = calc_func[c](A)
printA(A)