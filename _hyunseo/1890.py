import sys
from collections import deque

input = sys.stdin.readline


def move() :
    global robots
    ''' 컨베이어 벨트 회전 '''
    belt.appendleft(belt.pop())
    new_robots = deque()
    for idx, r in enumerate(robots) :
        if r == 2*N -1 :
            new_robots.append(0)
            continue
        if r + 1 == N-1 :
            continue
        new_robots.append(r + 1)
    robots = new_robots

def move_robot() :
    global robots
    new_robots = deque(robots)
    ''' 제일 먼저 올라간 로봇부터 이동'''
    
    for robot in robots :
        
        new_robots.popleft()
        next = robot + 1
        if 2*N == next :
            next = 0
        if belt[next] == 0 or next in new_robots:
            new_robots.append(robot)
            continue
        
        
        belt[next] -= 1
        if next == N-1 : continue
        else : new_robots.append(next)
    
    robots = new_robots

def put_new_robot() :
    if belt[0] > 0 and 0 not in robots :
        belt[0] -= 1
        robots.append(0)

def check_for_0() :
    count = 0
    for b in belt :
        if b == 0 :
            count += 1
            
    if count >= K :
        return True  # 게임 끗
    return False
        
def solve(N, K, belt) :
    robots = deque()
    time = 1
    while True :
        move()
        move_robot()
        put_new_robot()
        
        if check_for_0() :
            print(time)
            sys.exit()
        time += 1
    
    
    
    
N, K = map(int, input().split())  
belt = deque(list(map(int, input().split())))
robots = deque()
solve(N, K, belt)
