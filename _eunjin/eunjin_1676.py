# 입력 받기
N = int(input())


def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)


num = str(fact(N))

result = 0

#print("num:", num)

for i in range(len(num)-1, -1, -1):
    if num[i] != "0":
        break
    result += 1

print(result)
