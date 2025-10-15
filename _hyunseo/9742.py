import math
import sys


def get_exc(n) :
    tmp = 1
    while n != 1 :
        tmp *= n
        n -= 1
    return tmp

def get_answer(inp_, num) :
    original_num =num
    original = ''.join(inp_)
    # No Permutation
    if get_exc(len(inp_)) < num :
        print(f"{''.join(inp_)} {num} = No permutation")
        return
    answer = ""
    N = len(inp_)
    while len(answer) != N or inp_:
        if len(inp_) == 1 :
            answer += inp_.pop()
            continue
        n = len(inp_) - 1
        n = get_exc(n)
        for tmp in range(N+1) :
            if num == 0 :
                answer += inp_.pop(0)
                break
            if tmp*n < num <= (tmp+1)*n :
                popped_tmp = inp_.pop(tmp)
                answer += popped_tmp
                num -= tmp*n
                break
    print(f'{original} {original_num} = {answer}')

def solve():
    for line in sys.stdin:
        inp_ = line.strip().split()
        if not inp_:  # 혹시 빈 줄이면 무시
            continue
        inp_, num = inp_
        inp_ = list(inp_)
        inp_.sort()
        num = int(num)
        get_answer(inp_, num)
            

solve()
