from collections import deque
st = input()

# 그리디?

q = deque()

# B의 인덱스를 모두 큐에 넣기
for i in range(len(st)):
    if st[i] == "B":
        q.append(i)

answer = 0

# AB 쌍 맞추기
for i in range(len(st) - 1, -1, -1):
    if st[i] == "A":
        if q and q[-1] > i:  # B가 남아있고, 그 위치가 현재 A 이전일 때
            answer += 1
            q.pop()

# CB 쌍 맞추기
for i in range(len(st)):
    if st[i] == "C":
        if q and q[0] < i:  # B가 남아 있고, 그 위치가 현재 C 이후일 때
            answer += 1
            q.popleft()

print(answer)
