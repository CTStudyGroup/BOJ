N = int(input())
arr = list(input() for _ in range(N))

ans = 0
for word in arr:
    temp = []
    for i in range(len(word)):
        if temp and temp[-1] == word[i]:
            temp.pop()
        else:
            temp.append(word[i])

    if not temp:
        ans += 1

print(ans)
