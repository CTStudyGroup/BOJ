import sys
input = sys.stdin.readline

# 그냥 기댓값과 다른 문자의 개수를 세는건가???
# 뒤에서부터 보면서
def solve(string):
    N = len(string)
    stack = []
    answer = 0
    while string:
        curr = string.pop()
        if stack:
            if curr == "{":
                if stack[-1] == "}":  # {}인 경우
                    stack.pop()
                else:
                    stack.pop()  # {{인 경우
                    answer += 1
            else:  # }인 경우
                stack.append(curr)
        else:  # 스택이 빈 경우
            if curr == "{":
                answer += 1  # 현재 {를 }로 바꿔서 넣기
            stack.append("}")

    if stack:  # 스택에 }가 남아있는 경우, 안정적인 문자열이 아님
        answer += len(stack) // 2

    return answer

T = 1
while True:
    string = list(input().rstrip())
    if string[0] == '-':
        break
    answer = solve(string)
    print("{}. {}".format(T, answer))
    T += 1
