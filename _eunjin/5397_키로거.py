from collections import deque
import sys
input = sys.stdin.readline

# - : 커서 바로 앞 글자 제거
# < : 왼족으로 1칸 이동
# > : 오른쪽으로 1칸 이동
# 커서 기준 왼쪽에 입력된 비밀번호 추가

N = int(input())

def solve(string):
    left = deque()
    right = deque()
    for s in string:
        if s == "-":
            if left:
                left.pop()
        elif s == "<":
            if left:
                right.appendleft(left.pop())
        elif s == ">":
            if right:
                left.append(right.popleft())
        else:
            left.append(s)

    return ''.join(left) + ''.join(right)


for _ in range(N):
    inp = input().strip()
    print(solve(inp))

