from sys import stdin as s

s = open("txt/11899.txt", "r")

# 서로 다른 괄호열의 수를 구하면 ? -> ))(( 반례
# ( 경우 결과 +1, 카운트 + 1
# ) 경우 카운트이 있다면 결과 -1, 스택 -1 / 카운트이 없다면 결과 + 1

L = list(s.readline().strip())

cnt = 0
result = 0

for i in L:
    if i == ')':
        if cnt > 0:
            cnt -= 1
            result -=1
        else:
            result += 1
    elif i == '(':
        cnt += 1
        result += 1

print(result)

# 13분 20초
