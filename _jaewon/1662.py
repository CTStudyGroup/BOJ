# 스택을 사용
# 숫자는 문자열로 취급
# 숫자와 '('은 push
# ')'을 만나면 '(' 다음 숫자를 만날때까지 pop
# '()' 안에 있는 숫자를 반복해서 push

import collections

arr = str(input())
stack = collections.deque([])

for element in arr:
    if(element != ')'):
        stack.appendleft(element)
    else:
        inside = []

        # '('를 만날때까지 내부 element를 탐색
        while True:
            top = stack.popleft()
            if(top == '('):
                break
            else:
                inside.append(top)

        if(inside):
            loop = int(stack.popleft())
            array = inside * loop
            stack.appendleft(''.join(array))
        # '()' 이면 그냥 무시한다.
        else:
            stack.popleft()
            
print(len(''.join(stack)))