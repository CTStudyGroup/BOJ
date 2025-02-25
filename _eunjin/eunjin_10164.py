N, M, K = map(int, input().split())

row, col = N-1, M-1
x = 1
for i in range(N):
    for j in range(M):
        if x == K:
            row, col = i, j
        x += 1


#  1  2  3  4  5
#  6  7  8  9 10
# 11 12 13 14 15

# (가로 이동 수 + 세로 이동 수)C(가로 이동 수)
# n*(n-1)*(n-2) ... *(n-k+1) / k!


def nCk(n, k):
    ret = 1
    for i in range(k):
        ret = ret * (n-i)
    for i in range(1, k+1):
        ret = ret//i
    return ret


if K == 0:
    print(nCk(row+col, row))
else:
    v1 = nCk(row+col, row)
    row, col = N-1-row, M-1-col
    v2 = nCk(row+col, row)
    print(v1*v2)
