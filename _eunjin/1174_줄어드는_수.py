N = int(input())

total = []

def backtracking(n):
    temp = 0
    for i in range(len(arr)):
        temp += arr[i] * 10**i
    total.append(temp)

    for i in range(n + 1, 10):
        arr.append(i)
        backtracking(i)
        arr.pop()

for i in range(10):
    arr = [i]
    backtracking(i)

total.sort()

if N > len(total):
    print(-1)
else:
    print(total[N - 1])

