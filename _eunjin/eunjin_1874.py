N = int(input())


stack = []
stack.append(1)
x = 1

result = []
result.append("+")

for _ in range(N):
    n = int(input())
    # print("n:", n, ",stack:", stack, ", x:", x)

    if(stack):
        if(stack[-1] < n):
            if(x >= n):
                print("NO")
                exit()
            else:
                while(stack[-1] < n):
                    x += 1
                    stack.append(x)
                    result.append("+")

                stack.pop()
                result.append("-")

        else:
            while(stack[-1] >= n):
                stack.pop()
                result.append("-")

                if not stack:
                    break
    else:
        if(x >= n):
            print("NO")
            exit()
        else:
            x += 1
            stack.append(x)
            result.append("+")
            while(stack[-1] < n):
                x += 1
                stack.append(x)
                result.append("+")

            stack.pop()
            result.append("-")

print('\n'.join(result))
