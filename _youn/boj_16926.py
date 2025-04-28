def printA(A):
    for a in A:
        print(*a)

def rotate(A, N, M):
    tmpA = [[0]*M for _ in range(N)]
    start = 0

    while start < N//2 and start < M//2:
        i, j = start, start

        for j in range(start, M-1-start):
            tmpA[i][j] = A[i][j+1]   
                       
        for i in range(start, N-1-start):
            tmpA[i][M-1-start] = A[i+1][M-1-start]  
        
        for j in range(M-1-start, start, -1):
            tmpA[N-1-start][j] = A[N-1-start][j-1] 

        for i in range(N-1-start, start, -1):
            tmpA[i][start] = A[i-1][start] 
             
        start += 1 
    return tmpA

N, M, R = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
for _ in range(R):
    A = rotate(A, N, M)
printA(A)