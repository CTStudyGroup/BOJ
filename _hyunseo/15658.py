import sys

input = sys.stdin.readline

# 수의 개수 (2 <= <= 11)
N = int(input())
# 수의 나열
A = list(map(int, input().split()))
# 연산자 수 (+, -, x, %)
operative_cnt = list(map(int, input().split()))
answer = []
def dfs(op_cnt, idx,  total, log) :
    if idx == N :
        answer.append(total)
        print(f'log : {log} total : {total}')
        return
    for i in range(4) :
        if op_cnt[i] == 0 : continue
        op_cnt[i]-=1
        if i == 0:
            log.append("+")
            dfs(op_cnt, idx + 1, total + A[idx], log)
            log.pop()
        if i == 1:
            log.append("-")
            dfs(op_cnt, idx + 1, total - A[idx], log)
            log.pop()
        if i == 2:
            log.append("x")
            dfs(op_cnt, idx + 1, total*A[idx], log)
            log.pop()
        if i == 3:
            log.append("%")
            if total < 0 and A[idx] > 0:
                total = abs(total)
                dfs(op_cnt, idx+1, (-1)*(total//A[idx]), log)
            else :
                dfs(op_cnt, idx+1, total//A[idx], log)
            log.pop()
        op_cnt[i] += 1
dfs(operative_cnt, 1, A[0],[])
print(max(answer))
print(min(answer))
