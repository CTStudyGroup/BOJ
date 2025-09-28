# 순열을 청소할 수 있는가?
# 4개의 스택에 넣고 나중에 뺐을때 내림차순 정렬이 되는가
# 스택에 쌓을 때는 반드시 나보다 큰 값이 나의 위에 와야 한다.

N = int(input())
array = list(map(int, input().split()))

stacks = [[] for _ in range(4)]

printed = False
for element in array:
    flag = True
    for stack in stacks:
        if(len(stack) == 0 or stack[-1] < element):
            # 삽입 가능
            stack.append(element)
            flag = False
            break
    
    if(flag):
        print('NO')
        printed = True
        break

if(not printed):
    print('YES')
