import sys

num = 1
while True:
    s = input().strip()
    if s[0] == "-":
        break
    
    stack = []
    cnt = 0
    for ch in s:
        if ch == "{":
            stack.append(ch)
        else:  
            if stack:
                stack.pop()
            else:
                cnt += 1
                stack.append("{")
    
    cnt += len(stack) // 2
    print(f"{num}. {cnt}")
    num += 1
