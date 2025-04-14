from itertools import product

arr = list(map(int, input().split()))

# 입력된 카드의 시계수 구하기
def getclocknum(arr):
    clocknum = 9999
    for i in range(4):
        string = str(arr[i])
        for j in range(i + 1, 4):
            string += str(arr[j])
        for k in range(i):
            string += str(arr[k])

        if int(string) < clocknum:
            clocknum = int(string)

    return clocknum

my_clock = getclocknum(arr)


# 전체 가능한 카드의 시계수
total = []
for comb in product(range(1, 10), repeat=4):
    num = getclocknum(comb)
    if num not in total:
        total.append(getclocknum(comb))

for i in range(len(total)):
    if my_clock == total[i]:
        print(i + 1)
