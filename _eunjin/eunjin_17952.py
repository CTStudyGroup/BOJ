import sys
input = sys.stdin.readline

N = int(input())

stack = []  # 과제 점수, 소요 시간
answer = 0

# 과제가 주어지면 해당 과제 바로 1분 수행, 소요 시간 남았으면 stack에 넣기
# 과제가 주어지지 않으면 stack의 가장 위에 있는 과제 1분 수행
# 과제의 남은 시간이 0이 되면 stack에서 pop
for _ in range(N):
    command = input().split()
    if command[0] == "0":
        if stack:
            stack[-1][1] -= 1  # 가장 최근 과제 수행
            if stack[-1][1] == 0:  # 과제가 끝났으면
                answer += stack.pop()[0]
    else:  # 과제가 주어지면
        A, T = int(command[1]), int(command[2])
        if T == 1:  # 해당 과제 바로 수행
            answer += A
        else:
            stack.append([A, T])  # stack에 과제 추가
            stack[-1][1] -= 1  # 해당 과제 수행

print(answer)
