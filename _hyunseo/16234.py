'''
A는 나라에 사는 인구 수 Population

하루에 한번씩 인구 이동 move  -> 더이상 인구 이동이 없을때까지 지속

move는 
1. 국경선 공유하는 두 나라 (d = [위, 오른, 아래, 왼])
인구 차이가 L이상, R 이하이면 국경선 염
  2 . 인구 ㄱ이동
  3. 열려있는 인접 칸막 통해서 이동 가능 
  4. 총 인구수를 구하고
  5. 인구수 // 연합을 이루는 칸의 개수 -> 소수점 버림

구하는 것 : 이동 날짜
  
'''
import sys

input = sys.stdin.readline
from collections import deque


def bfs(i, j , visited) :
    q = deque()
    q.append((i, j))
    # 움직일 대상
    cities = []
    # 움직일 대상 총 인구 수
    population = 0
    visited[i][j] = 1
    # 인접 도시들 구하기
    while q :
        y, x = q.popleft()
        # 방문 표시, city 추가, 인구수에 추가
        
        population += A[y][x]
        cities.append([y, x])
        
        for dir in range(4) :
            ty, tx = y + d[dir][0], x + d[dir][1]
            if 0<= ty < N and 0 <= tx < N and visited[ty][tx] == 0 :
                if L<= abs(A[y][x] - A[ty][tx]) <= R :
                    q.append((ty, tx))
                    visited[ty][tx] = 1
                
    return population, cities

def move(population, cities) :
    flag = True
    city = len(cities)
    
    for y, x in cities :
        if A[y][x] != population // city :
            flag = False
            A[y][x] = population // city
    # 만약 변경 사항이 없다면 True 반환
    return flag

def solve() :
    time = 0
    # 변경이 없을 때까지 반복
    while time < 2000 :
        
        visited = [[0]*N for _ in range(N)]
        time_flag = False
        for i in range(N) :
            for j in range(N) :
                if visited[i][j] == 0 :
                    population, cities = bfs(i, j, visited)
                    flag = move(population, cities)
                    # 만약 변동 사항이 없다면 True flag
                    # 만약 한번이라도 변경된다면 time_flag 변경
                    if not flag :
                        time_flag = True
        if not time_flag :
            return time
        time += 1
                    
    return time


# N는 크기, L,R는 인구수 차이 끝값
N, L, R = map(int, input().split())
A = []
for _ in range(N) :
    A.append(list(map(int, input().split())))
d = [[-1,0], [0,1], [1,0], [0,-1]]

print(solve())
