from collections import deque

N = int(input())
matrix = [[0] * 52 for _ in range(52)]

# 0~51 인덱스 -> 알파벳으로 변환
IDX_TO_CHAR = {}
for i in range(26):
    IDX_TO_CHAR[i] = chr(i + 65)
for i in range(26, 52):
    IDX_TO_CHAR[i] = chr(i + 71)

# 알파벳 -> 0~51 인덱스로 변환
CHAR_TO_IDX = {}
for i in range(26):
    CHAR_TO_IDX[chr(i + 65)] = i
for i in range(26, 52):
    CHAR_TO_IDX[chr(i + 71)] = i


for _ in range(N):
    ch1, ch2 = input().split(" => ")
    idx1, idx2 = CHAR_TO_IDX[ch1], CHAR_TO_IDX[ch2]
    matrix[idx1][idx2] = 1

def bfs(start):
    q = deque()
    visited = [False] * 52
    ret = []

    visited[start] = True
    q.append(start)

    while q:
        curr = q.popleft()

        if curr != start:
            ret.append(curr)

        for i in range(52):
            if i == curr:
                continue
            if matrix[curr][i] and not visited[i]:
                visited[i] = True
                q.append(i)

    return sorted(ret)

# 0~51 모든 알파벳에 대해 bfs탐색해서 연결되어있는 알파벳 구하기
answer_cnt = 0
answer_arr = [[] for _ in range(52)]

for i in range(52):
    connected = bfs(i)
    answer_arr[i] = connected
    answer_cnt += len(connected)

print(answer_cnt)
for i in range(52):
    for j in answer_arr[i]:
        print(IDX_TO_CHAR[i], "=>", IDX_TO_CHAR[j])
