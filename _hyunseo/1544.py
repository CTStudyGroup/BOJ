from collections import deque

N = int(input())

word_set = []

for _ in range(N) :
    word = input().strip()
    flag = True
    for comp in word_set :
        
        if len(comp) == len(word):
            q = deque(word)
            
            for _ in range(len(word)) :
                
                if ''.join(q) == comp :
                    flag = False
                    continue
                q.append(q.popleft())
    if flag :
        word_set.append(word)

print(len(word_set))
