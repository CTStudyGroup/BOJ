st = input()

stack = []
for s in st:
    stack.append(s)

    if stack[-1] == "P":
        if len(stack) < 4:
            continue

        temp = ""
        for i in range(len(stack) - 4, len(stack)):
            temp += stack[i]

        if temp == "PPAP":
            stack.pop()
            stack.pop()
            stack.pop()

if len(stack) == 1 and stack[0] == "P":
    print("PPAP")
else:
    print("NP")
