import sys
input = sys.stdin.readline

string = input().strip()

# ()가 등장하기 전까지 쌓인 ( 의 개수만큼 조각이 생긴다
stack = []
answer = 0
for i in range(len(string)):
    if string[i] == "(":
        stack.append("(")
    else:
        if string[i - 1] == "(":  # 레이저인 경우
            stack.pop()  # 레이저 괄호 지우고
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)
