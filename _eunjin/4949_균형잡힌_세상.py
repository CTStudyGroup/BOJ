import sys
input = sys.stdin.readline
while True:
    string = input().rstrip()
    if string == ".":
        exit()
    # print(string)

    stack = []
    valid = True
    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")
        elif string[i] == "[":
            stack.append("[")
        elif string[i] == ")":
            if not stack or stack[-1] == "[":
                valid = False
                break
            stack.pop()
        elif string[i] == "]":
            if not stack or stack[-1] == "(":
                valid = False
                break
            stack.pop()
    if stack:
        valid = False

    if valid:
        print("yes")
    else:
        print("no")
