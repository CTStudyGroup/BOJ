from collections import deque

N, W, L = map(int, input().split())
truck = list(map(int, input().split()))

q = deque()
for _ in range(W):
    q.append(0)

answer = 0

# 모든 트럭이 큐를 거치기
idx = 0  # 현재 몇 번 트럭 이동할지
while idx < N:
    answer += 1
    q.popleft()  # 한 칸 이동

    if sum(q) + truck[idx] <= L:  # 새 트럭 들어가도 하중 제한 안넘는 경우
        q.append(truck[idx])
        idx += 1
    else:  # 새 트럭 못들어가는 경우
        q.append(0)  # 빈 칸 채우기

# 큐에 남은 트럭을 빼기
while q:
    answer += 1
    q.popleft()

print(answer)
