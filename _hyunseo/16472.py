import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())  # 인식 가능한 알파벳 종류의 최대 개수 (<= 26)
input_ = input().strip()  # 문자열


# 조기 종료
if len(set(input_)) <= N :
    print(len(input_))
    

# sliding window
l, r = 0, 0
s = set()
s.add(input_[l])
cnt = 1
answer = 0
dic = defaultdict(int)
dic[input_[l]] += 1
while True :
    r += 1
    if l == r :
        r += 1
        continue
    
    if r == len(input_)- 1 or l == len(input_) -1 :
        break
    s.add(input_[r])
    dic[input_[r]] += 1
    cnt += 1
    
    # 밀기 , r 더하기
    if len(s) <= N :
        answer = max(answer, cnt)
        
        
        
    # 당기기, L 당기기
    else :
        while len(s) > N :
            print(f'l : {l} r : {r} set : {s}')
            print(dic)
            dic[input_[l]] -= 1
            cnt -= 1
            if dic[input_[l]] == 0 :
                s.remove(input_[l])
            l += 1
        print(f' L 당기기 끗 : l : {l} r : {r} cnt : {cnt} set : {s}')
        
print(answer)
