import sys
from collections import deque


def solve(idx, repeat_num) :
    total = 0
    while input_[idx] != ")" :
        '''idx는 ( 다음부터 시작'''
        if input_[idx+1] == "(" :
            tmp, end = solve(idx+2, input_[idx])
            total += tmp
            idx = end
        else : 
            total += 1
            idx += 1
    return total* int(repeat_num), idx + 1

input_ = input().strip()
answer = 0

i = 0
while i < len(input_) -1  :
    if input_[i+1] == '(' :
        tmp, end = solve(i+2, input_[i])
        i = end
        answer += tmp
    else :
        answer += 1
        i += 1
if input_[-1] != ')' :
    answer += 1
print(answer)
