import sys
from collections import deque

input = sys.stdin.readline


T = int(input())

for t in range(T) :
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    answer = deque()
    diff = 0
    
    
    for log in logs :
        print(answer, diff)
        if len(answer) < 2 :
            answer.append(log)
        # log가 맨끝, 또는 맨 앞이랑 같을 경우에는, 같지 않은 쪽으로 붙이기. 
        elif answer[0] == log or answer[-1] == log :
            if answer[0] == log :
                diff = max(diff, abs(log - answer[-1]))
                answer.append(log)
            else :
                diff = max(diff, abs(log - answer[0]))
                answer.appendleft(log)
        # log는 순차적으로 증가하기 때문에, 더 answer의 양쪽 끝 중 더 작은 쪽에 붙이기
        elif answer[0] <  answer[-1] :
            diff = max(diff, abs(log-answer[0]))
            answer.appendleft(log)
        else :
            diff = max(diff, abs(log - answer[-1]))
            answer.append(log)
    diff = max(diff, abs(answer[0]-answer[-1]))
    print(diff)
    
