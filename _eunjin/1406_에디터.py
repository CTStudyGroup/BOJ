import sys
from collections import deque
input = sys.stdin.readline

start_str = input().strip()
M = int(input())

# 커서 기준 왼쪽 문자열, 오른쪽 문자열 각각에 대한 큐
left = deque()
right = deque()

for st in start_str:
    left.append(st)

for _ in range(M):
    cmds = list(input().split())
    cmd = cmds[0]

    if cmd == "L":  # 커서 왼쪽 이동
        if left:
            right.appendleft(left.pop())
    elif cmd == "D":  # 커서 오른쪽 이동
        if right:
            left.append(right.popleft())
    elif cmd == "B":
        if left:
            left.pop()
    else:
        st = cmds[1]
        left.append(st)

for elem in left:
    print(elem, end="")
for elem in right:
    print(elem, end="")
