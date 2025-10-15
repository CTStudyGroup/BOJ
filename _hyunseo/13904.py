import heapq
import sys
input = sys.stdin.readline


work = []

N = int(input())
last_day = 0

for _ in range(N) :
    d, w = map(int, input().split())
    last_day = max(last_day, d)
    
    heapq.heappush(work, (-w, -d))


# 총 과제 점수
answer = 0

# 역순으로 탐색
for day in range(last_day, 0, -1 ) :
  # tmp는 현재 사용되지 않은 과제들을 따로 저장
    tmp = []
    while work :

      # 제일 과제 점수가 큰 과제를 pop
        w, d= heapq.heappop(work)
        d, w = d*-1, w*-1

      # 과제 일수 지났으면 일단 무시
        if d < day : 
            tmp.append((-w, -d))
            continue

      # 과제 일수 지나지 않았으면 과제 점수에 포함시키고 break
        else :
            answer += w
            break

  # 사용되지 않은 과제 다시 추가 
    for t in tmp :
        heapq.heappush(work, t)
print(answer)
