N = int(input())
taste = []
for _  in range(N ): 
    taste.append(list(map(int, input().split())))
    
import sys
# N이 10 이하이기 때문에 bruteforce
from itertools import combinations

input = sys.stdin.readline

answer = sys.maxsize

# 쓴맛, 신맛 차이 구하는 함수 
def get_difference(list_) :
    C, B = 1, 0
    for c, b in list_ :
        C *= c
        B += b
    return abs(C- B)


""
# 사용할 개수 1개
for s, b in taste :
    answer = min(answer, abs(s-b))
    
# 사용할 개수 2~ 개
for n in range(2, N+1) :
    combin = (combinations(taste, n))
    for c in combin :
        answer = min(answer, get_difference(c))
        
        # 조기 종료
        if answer == 0 :
            break
print(answer)
