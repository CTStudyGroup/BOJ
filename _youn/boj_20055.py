from collections import deque

def isValid(v, robots, A):
    return v not in robots and A[v]>0

def moveRobots(robots, A, N):
    lr = len(robots)
    for _ in range(lr):
        v = robots.popleft()
        if isValid(v+1, robots, A):  
            v += 1
            A[v]-=1
        if v < N-1: robots.append(v)

def rotate(robots, A, N):
    A.insert(0, A.pop()) # rotate belt
    lr = len(robots)
    for _ in range(lr): # robots index + 1
        v = robots.popleft()+1
        if v < N-1: robots.append(v)

def solve(N, K, A):
    robots = deque([])
    ans = 0
    while A.count(0)<K:
        ans += 1
        rotate(robots, A, N) # (1) rotate
        moveRobots(robots, A, N) # (2) move robots
        if isValid(0, robots, A): # (3) add robot in start position
            robots.append(0)
            A[0] -= 1  
    return ans

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
print(solve(N, K, A))
