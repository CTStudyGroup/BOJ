N = int(input())
K = int(input())
arr = list(map(int, input().split()))

arr.sort()
diff = []
for i in range(N - 1):
    diff.append(arr[i + 1] - arr[i])

diff.sort()
print(sum(diff[:N - K]))
