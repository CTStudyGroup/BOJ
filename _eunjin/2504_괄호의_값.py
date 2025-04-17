string = input()

# (()[[]])([])
# +2*2+2*3*3+2*3
# 4 + 18 + 6

stack = []
mul = 1
answer = 0
for i in range(len(string)):
    if string[i] == "(":
        stack.append("(")
        mul *= 2
    elif string[i] == ")":
        if not stack or stack[-1] == "[":
            print(0)
            exit()
        if string[i - 1] == "(":
            answer += mul
        stack.pop()
        mul //= 2
    elif string[i] == '[':
        stack.append('[')
        mul *= 3
    else:
        if not stack or stack[-1] == "(":
            print(0)
            exit()
        if string[i - 1] == "[":
            answer += mul
        stack.pop()
        mul //= 3

if stack:
    print(0)
else:
    print(answer)
