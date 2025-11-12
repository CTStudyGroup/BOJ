import sys
from collections import deque

input = sys.stdin.readline
dic = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, 
       "C" : 100, "D" : 500, "M" : 1000 ,
       "IV" : 4, "IX" : 9, "XL" : 40,
       "XC" : 90, "CD" : 400, "CM" : 900}
rev = {}
for key, val in dic.items() :
    rev[val] = key

def to_num(a) :
    q = deque(a)
    result = 0
    while q :
        cur = q.popleft()
        if q and dic[cur] < dic[q[0]] : 
            cur += q.popleft()
        result += dic[cur]
    return result

dp = [0, [1], [1, 1], [1, 1, 1], [4], [5], [5, 1], [5, 1, 1], [5,1,1,1], [9]]
def to_string(n) :
    answer = ''
    if n >= 1000 :
        answer= 'M'*(n//1000)
        n %= 1000
    for i in range(2, -1, -1) :
        tmp = n // 10**i
        cur = dp[tmp]
        if cur == 0 : continue
        for c in cur :
            answer += rev[c*(10**i)]
            n = n -  c*(10**i)
            
    return answer


A = input().strip()

B = input().strip()

a, b = to_num(A), to_num(B)
print(a+b)
print(to_string(a+b))


