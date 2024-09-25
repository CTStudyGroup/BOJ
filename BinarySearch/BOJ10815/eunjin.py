# 입력 받기
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
sang = list(map(int, input().split()))

cards.sort()


def bs(x):
    global cards

    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if(cards[mid] > x):
            end = mid-1
        if(cards[mid] < x):
            start = mid+1
        if (cards[mid] == x):
            return 1
    return 0


for i in range(M):
    print(bs(sang[i]), end=" ")
