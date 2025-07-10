from collections import defaultdict
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
_dict = defaultdict(int)

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

# 백트래킹인가???
# 그냥 가능한 모든 문자열을 다 dict에 갖고 있기

def backtracking(y, x):
    global st
    if 1 <= len(st) <= 5:
        _dict[''.join(st)] += 1

    if len(st) > 5:
        return

    for i in range(8):
        ny = (y + dy[i]) % N
        nx = (x + dx[i]) % M

        st.append(matrix[ny][nx])
        backtracking(ny, nx)
        st.pop()

for y in range(N):
    for x in range(M):
        st = [matrix[y][x]]
        backtracking(y, x)

for _ in range(K):
    inp = input().strip()
    print(_dict[inp])

# # 백트래킹 시간 초과
# # arr로 넣었다 뺐다 하지말고 그냥 string으로 복사해서 넘겨버리기
# def dfs(y, x, st):
#     st += matrix[y][x]
#     _dict[st] += 1

#     if len(st) >= 5:
#         return

#     for i in range(8):
#         ny = (y + dy[i]) % N
#         nx = (x + dx[i]) % M

#         dfs(ny, nx, st[:])

# for y in range(N):
#     for x in range(M):
#         dfs(y, x, "")

# for _ in range(K):
#     inp = input().strip()
#     print(_dict[inp])
