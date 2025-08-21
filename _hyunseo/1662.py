# 메모리 초과 풀이
import sys
from collections import deque


def solve(idx, repeat_num) :
    d = deque()
    
    while input_[idx] != ")" :
        '''idx는 ( 다음부터 시작'''
        if input_[idx+1] == "(" :
            tmp_str, end = solve(idx+2, input_[idx])
            d.append(tmp_str)
            idx = end
        else : 
            d.append(input_[idx])
            idx += 1
    return str(''.join(d))* int(repeat_num), idx + 1

input_ = input()
answer = ''

i = 0
while i < len(input_) -1  :
    if input_[i+1] == '(' :
        tmp_str, end = solve(i+2, input_[i])
        i = end
        answer += tmp_str
    else :
        answer += input_[i]
        i += 1
if input_[-1] != ')' :
    answer += input_[-1]
print(answer)
print(len(answer))
