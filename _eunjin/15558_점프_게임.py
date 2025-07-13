from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
left = list(input().strip())
right = list(input().strip())
matrix = [left, right]

# bfs
visited = [[False] * N for _ in range(2)]
q = deque()
q.append((0, 0, 0))  # left/right, n, time

dk = [[0, 0, 1], [0, 0, -1]]  # 왼쪽 / 오른쪽
dn = [[1, -1, K], [1, -1, K]]  # 위 1칸, 아래 1칸, 위 K칸

while q:
    k, n, t = q.pop()

    for i in range(3):
        nk = k + dk[k][i]
        nn = n + dn[k][i]

        if 0 <= nk <= 1 and 0 <= nn:
            if nn > t:
                if nn >= N:
                    print("1")
                    exit()

                if matrix[nk][nn] == "1" and not visited[nk][nn]:
                    q.append((nk, nn, t + 1))
                    visited[nk][nn] = True

print("0")
