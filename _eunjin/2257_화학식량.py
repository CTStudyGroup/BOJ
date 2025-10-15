string = input()

# 스택 문제
stack = []

for char in string:
    if char == "H":
        stack.append(1)
    elif char == "C":
        stack.append(12)
    elif char == "O":
        stack.append(16)
    elif char == "(":
        stack.append(0)
    elif char == ")":  # 괄호 구간 닫기, 가장 최근 괄호 열린 구간까지의 화학식량 합산
        temp = 0
        while stack and stack[-1] != 0:  # 0이 나올 때까지 pop
            temp += stack.pop()
        stack.pop()  # 0을 pop
        stack.append(temp)  # 괄호 구간의 화학식량 다시 넣기
    else:  # 숫자 나오면 stack의 가장 끝에 담긴 값에 곱하기
        stack.append(stack.pop() * int(char))

print(sum(stack))
