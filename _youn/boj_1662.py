import sys

def solve(S):
    stack, cnt = [], 0
    for i in range(len(S)):
        if S[i] == ')':
            tmp, num = stack.pop()
            cnt = tmp + num*cnt
        elif S[i] == '(':
            cnt -= 1
            stack.append((cnt, int(S[i-1])))
            cnt = 0
        else: cnt += 1
    return cnt

S = list(sys.stdin.readline())[:-1]
print(solve(S))