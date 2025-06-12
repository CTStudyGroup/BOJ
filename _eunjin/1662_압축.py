string = list(input())

# 스택
stack = []
cnt = 0
before = ""

# (이 나올 때마다 스택에 지금까지의 길이와 K를 저장
# )이 나올 때마다 스택에서 하나 빼서 K만큼 현재 구간 반복하고 기존 길이 더하기

for s in string:
    if s == "(":
        stack.append((cnt - 1, before))  # 현재까지의 길이, K
        cnt = 0
    elif s == ")":
        temp = stack.pop()
        cnt = cnt * temp[1] + temp[0]  # 압축 풀어서 나온 길이 + 기존의 길이
    else:  # 숫자인 경우
        cnt += 1
        before = int(s)

print(cnt)
