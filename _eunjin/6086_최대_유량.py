import sys
from collections import deque
input = sys.stdin.readline

# 파이프의 정보 수
n = int(input())

# A -> 0, Z -> 51, 나머지 알파벳 -> 1~50
alphabets = ['A'] + [chr(i + ord('a')) for i in range(26)] + [chr(i + ord('B')) for i in range(25)]
alphabets_dict = dict()
for idx, alphabet in enumerate(alphabets):
    alphabets_dict[alphabet] = idx

# 파이프 정보 입력
pipes = [[0] * 52 for _ in range(52)]
for _ in range(n):
    pipe_1, pipe_2, flow = input().split()
    pipes[alphabets_dict[pipe_1]][alphabets_dict[pipe_2]] += int(flow)
    pipes[alphabets_dict[pipe_2]][alphabets_dict[pipe_1]] += int(flow)

# 최대 유량 탐색
total_flow = 0
while True:
    q = deque()
    parents = [-1] * 52

    q.append(0)
    parents[0] = 0

    # 'A'에서 출발하여 'Z'에 도착할 수 있는 방법 탐색
    while q and parents[51] == -1:
        cur = q.popleft()
        for nxt in range(52):
            if pipes[cur][nxt] > 0 and parents[nxt] == -1:
                q.append(nxt)
                parents[nxt] = cur

    # 더 이상 'Z'에 도착할 수 없다면 종료
    if parents[51] == -1:
        break

    # 해당 방법으로 흘려보낼 수 있는 유량 탐색
    max_flow = 10 ** 3
    idx = 51
    while idx != 0:
        max_flow = min(max_flow, pipes[parents[idx]][idx])
        idx = parents[idx]

    # 해당 유량은 더 이상 이용 불가
    idx = 51
    while idx != 0:
        pipes[parents[idx]][idx] -= max_flow
        idx = parents[idx]

    total_flow += max_flow

print(total_flow)
