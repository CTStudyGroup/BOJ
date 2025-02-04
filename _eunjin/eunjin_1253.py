N = int(input())

arr = list(map(int, input().split()))
arr.sort()


def search(i):
    global arr
    left = 0
    right = N-1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        if arr[left]+arr[right] == arr[i]:
            return True
        elif arr[left]+arr[right] > arr[i]:
            right -= 1
        else:
            left += 1

    return False


cnt = 0
for i in range(N):
    # print("n:", arr[i], ", sarch:", search(i))
    if search(i):
        cnt += 1
print(cnt)
