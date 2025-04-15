# 완전 탐색
# 포인터 두개로 숫자 부분만 추적하기
N = int(input())
words = list(input().strip() for _ in range(N))
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

number_list = []

for word in words:
    temp = ""
    for char in word:
        if char in numbers:
            temp += char
        else:
            if temp:
                number_list.append(int(temp))
                temp = ""

    if temp:
        number_list.append(int(temp))

for n in sorted(number_list):
    print(n)

