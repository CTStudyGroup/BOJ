H, W = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = W-1
lmax = arr[left]
rmax = arr[right]
answer = 0

while left < right:
    if lmax < rmax:
        left += 1
        lmax = max(lmax, arr[left])
        answer += max(0, lmax-arr[left])
    else:
        right -= 1
        rmax = max(rmax, arr[right])
        answer += max(0, rmax-arr[right])

print(answer)
