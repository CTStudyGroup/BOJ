import sys
input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))

stack = []
answer = []
curr = 1
possible = True

for i in range(N):
    x = arr[i]

    while curr <= x:
        stack.append(curr)
        answer.append("+")
        curr += 1

    if stack[-1] == x:
        stack.pop()
        answer.append("-")
    else:
        possible = False
        break

if possible:
    print('\n'.join(answer))
else:
    print("NO")

