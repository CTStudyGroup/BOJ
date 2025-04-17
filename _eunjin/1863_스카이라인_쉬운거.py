import sys
input = sys.stdin.readline
N = int(input())
height = [list(map(int, input().split())) for _ in range(N)]

# stack
# 입력 받은게 stack의 마지막 높이보다 높으면 stack에 추가
# 작으면 stack의 마지막 높이가 같거나 빌 때까지 pop
stack = []
answer = 0
for idx, cord in enumerate(height):
    x, y = cord[0], cord[1]
    if stack:
        if y > stack[-1]:
            stack.append(y)
        elif y < stack[-1]:
            while stack and stack[-1] >= y:
                k = stack.pop()
                if k > y:
                    answer += 1
            stack.append(y)
            # print("answer:", answer)
    else:
        stack.append(y)
    # print("idx:", idx, ", y:", y, "stack: ", stack)

while stack:
    n = stack.pop()
    if n > 0:
        answer += 1
print(answer)
