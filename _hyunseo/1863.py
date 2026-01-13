'''
heapq로 y 좌표를 관리해볼까나?

1, 1에서 1이 heapq으로 들어감 건물 하나 추가
2, 2에서는 제일 작은 것보다 크니 건물 하나 추가
5, 1에서 제일 큰 것보다는 작지만, 제일 작은 것보다는 큼. 건물 하나 추가 안됨.
    근데 큰 애는 빠져야 함. heap에서 2 빼 -> [1] 남아있음
    
6,3 에서 제일 작은 것보다 큼. heap에 넣어 (건물 하나 추가 3 )
8,1 에서 제일 큰 것 보다 작음. heap에서 3 빼
    근데 기존 heapq에 있던 거랑 같아서 건물은 추가 안함
11,0 에서 제일 큰 것보다 작음. 근데 0은 특수 경우라 heap에서 다 빼. 건물 추가 없어
-> 첫번쨰 뭉치에서 3개의 건물(최소)

15,2 에서 heap 비어있어서 2 추가(건물 하나 추가) [2]

17,3 에서 heap 최대 값보다 큼. 3 추가(건물 하나 추가) [2, 3]

20,2 에서 건물 하나 빼. 근데 [2] 랑 키 똑같으니까 건물 추가 X

22,1 에서 deque의 값보다 작아서 건물 하나 추가 (2는 빠지고) 

-> 두번쨰 뭉치에서 3개


[2,5] -> 3이 들어와
총 6개

deque네..
y_q = deque()
for _ in range(lst) :
    x, y = 뭐시기
    
    만약 q is empty :
        건물 하나 추가
        q.append(y)
        continue
        
    만약 q[-1] < y :
        q.append(y)
        건물 하나 추가
        continue
    만약 q[-1] > y :
        while q or q[-1]> y :
            q.pop()
        q.append(y)
        건물 하나 추가
deque로 y 좌표를 관리해보면? 

'''
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

buildings = []
answer = 0
q = deque()


for _ in range(N) :
    buildings.append(list(map(int, input().split())))
buildings.sort()
for x, y in buildings :
    # 바닥 밀착
    if y == 0 :
        q = deque()
        continue
    
    # 아직 빌딩이 없음
    if not q :
        q.append(y)
        answer += 1
        continue
    
    # 더 큰 건물
    elif q[-1] < y :
        q.append(y)
        answer += 1
        continue
    
    
    
    # 사이에 껴있는 건물
    elif q[-1] > y :
        while q and q[-1] > y :
            q.pop()
        if not q :
            q.append(y)
            answer += 1
            continue
        
        if q and q[-1] == y :
            continue
        
        if q and q[-1] < y :
            q.append(y)
            answer += 1
    
print(answer)
