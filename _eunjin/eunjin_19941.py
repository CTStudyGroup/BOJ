N, K = map(int, input().split())
string = input()

used = [False]*N

for i in range(N):
    if string[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0 <= j < N:
                if string[j] == 'H' and not used[j]:
                    used[j] = True
                    break

# print(used)
print(sum(used))
