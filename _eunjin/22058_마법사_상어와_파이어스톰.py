import sys
import copy
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
matrix = []
for _ in range(2**N):
    arr = list(map(int, input().split()))
    matrix.append(arr)

L = map(int, input().split())

def print_matrix(mat):
    print("------")
    print('\n'.join(' '.join(map(str, row)) for row in mat))

# 2^l 크기로 나눠서 90도 회전
def rotate(l):
    global matrix
    size = 2**l
    temp_matrix = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for y in range(0, 2**N, size):
        for x in range(0, 2**N, size):
            for i in range(size):
                for j in range(size):
                    temp_matrix[y + j][x + size - 1 - i] = matrix[y + i][x + j]

    matrix = temp_matrix

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def reduce():
    global matrix
    temp_matrix = copy.deepcopy(matrix)
    for y in range(2**N):
        for x in range(2**N):
            if matrix[y][x] <= 0:
                continue
            cnt = 0
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < 2**N and 0 <= nx < 2**N:
                    if matrix[ny][nx]:
                        cnt += 1
            if cnt < 3:
                temp_matrix[y][x] -= 1
    matrix = temp_matrix


for cmd in L:
    rotate(cmd)
    reduce()
    # print_matrix(matrix)

visited = [[False] * 2**N for _ in range(2**N)]
sm = 0
largest = 0
for y in range(2**N):
    for x in range(2**N):
        sm += matrix[y][x]
        if matrix[y][x]:
            if not visited[y][x]:
                q = deque()
                q.append((y, x))
                visited[y][x] = True
                seg = 0

                while q:
                    cy, cx = q.popleft()
                    seg += 1

                    for i in range(4):
                        ny, nx = cy + dy[i], cx + dx[i]
                        if 0 <= ny < 2**N and 0 <= nx < 2**N:
                            if not visited[ny][nx] and matrix[ny][nx]:
                                q.append((ny, nx))
                                visited[ny][nx] = True

                largest = max(seg, largest)

print(sm)
print(largest)
