'''
N 명의 고객들은 계산대에 있음

K개의 계산대가 있음
계산대에 온 사람들은 가장 빨리 다음으로 계산할 수 있는 곳에 감.

안내원이 고객을 계ㅏ산대로 안내할 때, 만약 계산대 대기 시간이 도일하면
번호가 작은 계산대로 안내함.

계산을 마치면 쇼핑몰을 아예 빠져 나감

if 계산을 마친 고객의 시간이 동일하면 출구에 가까운 높은 번호 계산대의 고객부터 먼저 빠져나감. 

물건 계산하는 데에는 종류 관계 없이 1 분 소요

-> N명의 정보에 대해서, 빠져나오는 순서.

쇼핑몰 빠져나가는 회원 번호 순서를 구하는 게 목적

deque겠죠

N = 10, k = 3일 때

123, 4 -> heap에 (0+4 (종료 시간), -1, 회원 번호)
21, 5 -> heapq에 (0+5(종료시간), -2, 21)
34, 14 -> heapq에 (14, -3, 34)
56, 1 -> heapq에서 (4, 1, 123)빼.[4] = 123 넣고
            heapq에 (4+1, 1, 56) 넣어

45, 7 -> heap에서 (5, -2, 21) 빼고, [5] =21 넣고
            heapq에( 5 + 7, -2, 45) 넣어
            
723, 5 -> heap에서 (5, -1, 56) 빼고 [5] = [21, 56] ㅁㅁㅁㅁㅁ
            heapq에 (5+5, -1, 723) 넣어
            
55, 7 -> heap에서 (10, -1, 723) 빼고 [10] = 723
            heapq에 (10+7, -1, 55)

13, 5 -> heapq에서 (12, -2, 45) 빼고 [12] = 45
            heapq에 (17, -2, 13) 넣어
910, 10 -> heap1에서 (17, -2, 13 ) 빼고 [17] = [13]
            heapq에(27, -2, 910) 넣어

73, 3-> heap에서 (17, -1, 55) 빼고 [17] = [13, 55]
            heap에 (20, -1, 73) 넣어
            
            
나머지 heap 순서대로 빼서 넣어
그리고 끝나는 시간은 sort하게 따로 모아(over_time)             
defaultdic에 [마친 시간] = 회원 번호로 list 로 정리
'''

import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

N, k = map(int, input().split())
line = []
for _ in range(N) :
    line.append(list(map(int, input().split()))) # 회원번호, 구입 물건 수 (i, w)
    # 회원 번호 i는 안 겹침

q = []
dic = defaultdict(list)
fin= set()
for i in range(k) :
    if i >= N :
        break
    # 끝나는 시간, 계산대 번호(역순으로), 회원 번호
    heapq.heappush(q, [line[i][1], (i+1), line[i][0]])
answer = 0
idx = 1
# k가 N보다 큰 경우를 고려해야할 수도... -> 찐
if k >= N :
    while q :
        time, cashier, id = heapq.heappop(q)
    
        dic[time].append([-cashier, id])
        fin.add(time)
    answer = 0
    idx = 1
    for t in sorted(fin) :
        dic[t].sort(key=lambda x: x[0])
        for t, id in dic[t] :
            answer += (idx * id)
            idx += 1
    print(answer)
    sys.exit()

for i, w in line[k:] :
    time, cashier, id = heapq.heappop(q)
    
    dic[time].append([-cashier, id])
    fin.add(time)
    
    heapq.heappush(q, [time + w, cashier, i])

while q :
    time, cashier, id = heapq.heappop(q)
    
    dic[time].append([-cashier, id])
    fin.add(time)




answer = 0
idx = 1
for t in sorted(fin) :
    dic[t].sort(key=lambda x: x[0])
    for t, id in dic[t] :
        answer += (idx * id)
        idx += 1
print(answer)
