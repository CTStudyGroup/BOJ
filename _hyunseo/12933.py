import sys
from collections import deque
input = sys.stdin.readline

sound = list(input().strip())
s = len(sound)

quack = ['q', 'u', 'a', 'c', 'k']

waiting_duck = deque()
quacking_duck = deque()
duck_arr = [-1] # [오리번호] = 끝난 idx


for idx in range(s) :
    # q 마주친 경우
    if sound[idx] == 'q' :
        # 기다리는 오리가 없는 경우 
        if not waiting_duck :
            # 새로운 오리 추가
            quacking_duck.append(len(duck_arr))
            duck_arr.append(0)
        # 기다리는 오리가 있는 경우
        else :
            duck = waiting_duck.popleft()
            quacking_duck.append(duck)
            duck_arr[duck] = 0
        continue
    
    # q가 아닌 다른 문자를 마주친 경우


    # 근데 소리내는 오리가 없는 경우
    if not quacking_duck :
        print(-1)
        exit()
    # 소리내는 오리가 있는 경우
    else :
        flag = True
        for duck in list(quacking_duck) :
            if sound[idx] == quack[(duck_arr[duck] + 1 )%5]:
                flag = False
                duck_arr[duck] += 1
              
                # quack 끝난 경우
                if duck_arr[duck] == 4 :
                    waiting_duck.append(duck)
                    quacking_duck.remove(duck)
                break
        # 소리 내고 있는 오리 중에서 다음 sound를 낼 수 있는 오리가 없는 경우 -> sound[idx] = C인데, 오리들은 q, quac 이런 소리 냈을 경우 
        if flag :
            print(-1)
            exit()
            
for tmp in range(1, len(duck_arr)) :
    # 오리 중 중간에 소리가 끊긴 오리가 있는 경우
    if duck_arr[tmp] != 4 :
        print(-1)
        exit()
# 모두다 소리를 잘 낸 경우, 처음에 추가했던 idx=0 제외하고 출력
print(len(duck_arr)-1)
