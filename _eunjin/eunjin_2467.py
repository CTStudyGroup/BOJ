import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N-1

min_value = abs(arr[left]+arr[right])
ans_left = left
ans_right = right

while(left < right):
    temp = arr[left]+arr[right]

    if abs(temp) < min_value:
        min_value = abs(temp)
        ans_left = left
        ans_right = right

        if min_value == 0:
            break

    if temp < 0:
        left += 1
    else:
        right -= 1

print(arr[ans_left], arr[ans_right])
