N = int(input())
expr = input().strip()
values = [float(input()) for _ in range(N)]

stack = []
for ch in expr:
    if ch.isalpha():  # A~Z
        stack.append(values[ord(ch) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)

print(format(stack[0], ".2f"))
