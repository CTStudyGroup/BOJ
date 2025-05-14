def flip(i, j, check):
    for x in range(i,i+3):
        for y in range(j, j+3):
            check[x][y] = not check[x][y]
        
def solve(A, B, N, M):
    if N < 3 and M < 3 and A!=B: return -1
    check = [[A[i][j]!=B[i][j] for j in range(M)] for i in range(N)]
    ans = 0
    for i in range(N-2):
        for j in range(M-2):
            if check[i][j]:
                flip(i, j, check)
                ans += 1
    return ans if check == [[False]*M for _ in range(N)] else -1

N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
print(solve(A, B, N, M))