# 251127 : [BOJ 17214] 다항 함수의 적분

from collections import deque


def juk(n, k) :
    # n*X**
    
    # n이 0이면 상수임
    if n == 0 and k == 0 :
        return 'W'
    tmp = k +1
    flag = n//tmp
    ans = str(n//tmp)
    for _ in range(tmp) :
        ans += 'x'
    if flag == 1 :
        return ans[1:]
    return ans

S = input().strip()
q = deque(S)

answer = ''
import re

while q :
    
    # 맨 앞이 숫자
    if q[0] in '0123456789':
        n = ''
        while q and q[0] in '0123456789' :
            n += q.popleft()
        n = int(n)
        x = 0
        while q and q[0] == 'x' :
            q.popleft()
            x += 1
        answer += juk(n, x)
        continue

    # 맨 앞이 x
    if q[0] == 'x' :
        n = 1
        x = 0
        while q and q[0] == 'x' :
            q.popleft()
            x += 1
        answer += juk(n, x)
        continue
    
    # 연산자
    answer += q.popleft()

if answer[-1] != 'W' :
    answer += "+W"
print(answer)
