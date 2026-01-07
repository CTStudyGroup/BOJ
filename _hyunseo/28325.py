import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

def get(num) :
    return (num + 1) // 2

cnt = 0
answer = 0
first = -1
for idx, val in enumerate(arr) :
    if val != 0 :
        if first == -1 :
            first = idx
            answer += val
            cnt = 0
        else :
            answer += val
            answer += get(cnt)
            cnt = 0
    else :
        
        cnt += 1
answer += get(cnt + first)

print(answer)
