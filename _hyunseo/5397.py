'''
비밀번호 창에 입력하는 글자를 얻음.

키로거는 사용자가 키보드를 누른 명령을 모두 기록
강산이가 비번 입력 시 -> 화살표, 백스페이스 누르면 정확한 비번 get

강산이가 비번 창에서 입력한 키를 주었을 때, 강산이가 비번 알아내는 프로그램
강산은
알파벳 대문자,소문자,숫자, 백스페이스, 화살표
'''
from collections import deque
# number of Test casees
N = int(input())

for _ in range(N) :
    # maximum length L <=1000000 String
    # 백스페이스는 "-"로 대체
    # 커서의 앞에 글자 존재, 글자 삭제
    # 화살표는 < > 로 주어짐. 
    typed = input()
    left_ans, right_ans = deque(), deque()
    for t in typed :
        # print("t", t)
        #커서 이동
        if t  == "<" :
            if left_ans :
                right_ans.appendleft(left_ans.pop())
            continue
        if t == ">" :
            if right_ans :
                left_ans.append(right_ans.popleft())
            continue
        if t == "-" :
            if left_ans :
                left_ans.pop()
            continue
        
        left_ans.append(t)
    print(''.join(left_ans) + ''.join(right_ans))
