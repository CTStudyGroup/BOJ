from sys import stdin as s
from collections import deque
s = open('txt/17952.txt', 'r')

N = int(s.readline())

subject = [s.readline() for _ in range(N)]

q = deque()

last_time = 0

result = 0

for i in range(N):
    if subject[i][0] != '0':
        if last_time > 0: # 만약 남은 과제가 진행중이라면 ?
            q.append([score, last_time])
        _, score, t = map(int, subject[i].split())
        last_time = t-1 #받자마자 바로 함
    else:
        if last_time == 0 and q: #작업이 끝났고,큐에 대기가 있다면 ?
            score, t = q.pop()
            last_time = t

        last_time -= 1

    if last_time == 0: # 과제가 다끝났을 경우
        result += score
print(result)

# 26m 17s