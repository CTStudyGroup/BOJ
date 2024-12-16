import sys
input = sys.stdin.readline


def customRound(n):
    if(n-int(n)) >= 0.5:
        return int(n)+1
    else:
        return int(n)


n = int(input())
if n == 0:
    print(0)
    exit()


arr = [int(input()) for _ in range(n)]

if n > 0 and n < 4:
    print(customRound(sum(arr)/n))
    exit()


cut = customRound(n * 0.15)
# print(cut)
arr.sort()

arr = arr[cut:-cut]
print(customRound(sum(arr)/(n-cut*2)))
