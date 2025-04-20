from itertools import product

string = input()

# 괄호 인덱스 쌍을 먼저 구하고
# 각 쌍마다 제거o / 제거x 경우 나눠서 보기?
arr = []  # 괄호 리스트
stack = []  # (의 인덱스
for i in range(len(string)):
    if string[i] == "(":
        stack.append(i)
    if string[i] == ")":
        arr.append((stack.pop(), i))

answer = set()

for comb in list(product(range(0, 2), repeat=len(arr))):
    valid = []  # 출력할 괄호 인덱스
    for i in range(len(comb)):
        if comb[i]:
            valid.append(arr[i][0])
            valid.append(arr[i][1])
    temp = ""
    for j in range(len(string)):
        if string[j] in ["(", ")"]:
            if j in valid:
                temp += string[j]
        else:
            temp += string[j]

    if temp != string:
        answer.add(temp)


answer = sorted(answer)
print('\n'.join(answer))
