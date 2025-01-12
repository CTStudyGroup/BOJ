total = input()
string = list(input())
l = len(string)

stack = []
for i in total:
    stack.append(i)
    if stack[-l:] == string:
        for _ in range(l):
            stack.pop()

if(stack):
    print(''.join(stack))
else:
    print("FRULA")
