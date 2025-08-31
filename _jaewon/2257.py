# 1. '('을 만나면 -> 스택에 집어 넣음
# 2. ')'을 만나면 -> '('을 만날 때까지 스택 pop
# 2-1. pop된 원소들을 임시 큐에 저장
# 2-2. )을 만난 다음 바로 뒤가 숫자이면 해당 숫자만큼 반복
# 3. 숫자를 만나면 -> 결과 += 앞에 있는 원소 * 숫자

import collections
chemical = input().strip()

numbers = ['2','3','4','5','6','7','8','9']
result = 0
index = 0 
stack = collections.deque([])
while(index < len(chemical)):
    if(chemical[index] == '('):
        stack.append('(')
    elif(chemical[index] == ')'):
        value = 0
        while(stack[-1] != '('):
            value += int(stack.pop())
        stack.pop()
        stack.append(value)
    elif(chemical[index] == 'C'):
        stack.append(12)
    elif(chemical[index] == 'H'):
        stack.append(1)
    elif(chemical[index] == 'O'):
        stack.append(16)
    else:
        # 숫자인 경우
        value = int(stack.pop())
        stack.append(value * int(chemical[index]))
    index += 1

print(sum(stack))
