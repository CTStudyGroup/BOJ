# 입력 받기
N = int(input())

x = 0

value = 0


def isNum(n):
    string = str(n)
    if(len(string) <= 2):
        return False

    before = False
    result = 0
    for elem in str(n):
        if elem == "6" and before:
            result += 1
        elif elem == "6" and not before:
            result = 1
            before = True
        elif result < 3:
            result = 0

    return result >= 3


while(x < N):
    while(True):
        value += 1
        if(isNum(value)):
            x += 1
            break

print(value)
