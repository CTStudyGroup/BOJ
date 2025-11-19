n, k = map(int, input().split())

l =1
r = n + 2

while l < r :
    print(f'l  {l} r: {r}')
    mid = (l + r) // 2
    tmp = mid*(n+2-mid)
    if tmp == k :
        print("YES")
        exit()
    if tmp > k :
        r = mid
    if tmp < k :
        l = mid + 1
print("NO")
