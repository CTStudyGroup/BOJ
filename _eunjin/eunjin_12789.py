N = int(input())

arr = list(map(int, input().split()))

curr = 0
stack = []


for x in arr:
    if x == curr+1:
        curr = x

        while(stack):
            if stack[-1] == curr+1:
                curr = stack.pop()
            else:
                break
    else:
        stack.append(x)

while(stack):
    x = stack.pop()

    if x == curr+1:
        curr = x
    else:
        print("Sad")
        exit()

print("Nice")

# 7
# 4 3 2 1 7 6 5
