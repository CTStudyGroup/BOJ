string = input()

num0 = 0
num1 = 0

for s in string:
    if s == "0":
        num0 += 1
    else:
        num1 += 1

num0 = num0 // 2  # 사용 가능한 0의 개수
num1 = num1 // 2  # 제거 가능한 1의 개수

answer = ""

for s in string:
    if s == "0":
        if num0 > 0:
            answer += "0"
            num0 -= 1
    else:
        if num1 > 0:
            num1 -= 1
        else:
            answer += "1"

print(answer)
