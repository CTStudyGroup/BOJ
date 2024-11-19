# 입력 받기
T = int(input())

for i in range(T):
    string = input()

    num = 0
    isVPS = True

    for s in string:
        if s == "(":
            num += 1
        else:
            num -= 1

        if num < 0:
            isVPS = False
            break
    if not num == 0:
        isVPS = False

    if isVPS:
        print("YES")
    else:
        print("NO")
