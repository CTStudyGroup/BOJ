import sys
from collections import deque

input = sys.stdin.readline
def turn_first_wheel(direction, spun) :
    if 2 not in spun :
        spun.add(2)
        if wheel1[2] != wheel2[-2] :
            turn_second_wheel(-1*direction, spun)
    if direction == 1: 
        wheel1.appendleft(wheel1.pop())
    else :
        wheel1.append(wheel1.popleft())
        
def turn_second_wheel(direction, spun) :
    if 1 not in spun :
        spun.add(1)
        if wheel1[2] != wheel2[-2] :
            turn_first_wheel(-1*direction, spun)
    if 3 not in spun :
        spun.add(3)
        if wheel3[-2] != wheel2[2] :
            turn_third_wheel(-1*direction, spun)
    if direction == 1: 
        wheel2.appendleft(wheel2.pop())
    else :
        wheel2.append(wheel2.popleft())
        
               
def turn_third_wheel(direction, spun) :
    if 2 not in spun :
        spun.add(2)
        if wheel2[2] != wheel3[-2] :
            turn_second_wheel(-1*direction, spun)
    if 4 not in spun :
        spun.add(4)
        if wheel4[-2] != wheel3[2] :
            turn_fourth_wheel(-1*direction, spun)
    if direction == 1: 
        wheel3.appendleft(wheel3.pop())
    else :
        wheel3.append(wheel3.popleft())    

def turn_fourth_wheel(direction, spun) :
    if 3 not in spun :
        spun.add(3)
        if wheel3[2] != wheel4[-2] :
            turn_third_wheel(-1*direction, spun)
            
    if direction == 1: 
        wheel4.appendleft(wheel4.pop())
    else :
        wheel4.append(wheel4.popleft())
        
        
# 바퀴 선언
wheel1 = deque(input().strip())
wheel2 = deque(input().strip())
wheel3 = deque(input().strip())
wheel4 = deque(input().strip())

K = int(input())
for _ in range(K ) :
    num, direction = map(int, input().split())
    # wheel_num은 1~4, direction은 1이 시계방향, -1이 반시계
    if num == 1 :
        turn_first_wheel(direction, {1})
    elif num == 2 :
        turn_second_wheel(direction, {2})
    elif num == 3 :
        turn_third_wheel(direction, {3})
    else :
        turn_fourth_wheel(direction, {4})

answer = 0 
if wheel1[0] =="1" :
    answer += 1
if wheel2[0] == "1" :
    answer += 2
if wheel3[0] == "1" :
    answer += 4
if wheel4[0] == "1" :
    answer += 8
print(answer)
