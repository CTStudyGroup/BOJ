# 입력 받기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


def binarySearch(arr, x):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left+right)//2

        if(arr[mid] < x):
            left = mid + 1

        if(arr[mid] > x):
            right = mid - 1

        if(arr[mid] == x):
            return 1

    return 0


A = sorted(A)

for i in range(M):
    print(binarySearch(A, B[i]))
