from sys import stdin as s
s = open("txt/2257.txt", "r")

# 입력받은 값이 문자열이라면 ? keep
# 열린괄호 라면 ? keep
# 닫힌괄호 들어오면 ? 스택에서 열린 괄호까지 다뺌, 빼고 계산된 값을 다시 넣어주기
# 숫자라면 ? 스택 값 빼고 곱하기

string = list(s.readline().strip())
stack = []
chemical = {'C':12,'O':16,'H':1}
for i in string:
    if i == '(':
        stack.append('(')
    elif i in chemical:
        stack.append(chemical[i])
    elif i == ")":
        sum_value = 0
        while 1:
            value = stack.pop()
            if value == '(':
                stack.append(sum_value)
                break
            elif type(value) == int:
                sum_value += value
    else:
        stack.append(stack.pop()*int(i))
print(sum(stack))