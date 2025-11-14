N = int(input())
sp = []
for _ in range(N) :
    sp.append(int(input()))
total = sum(sp)

j = 0
cur, max_ = 0, 0

for i in range(N) :
    while cur <=  total // 2 :
        print(f'i : {i} j : {j} cur : {cur}')
        max_ = max(max_, cur)
        
        
        
        cur += sp[j]
        j = (j+1) % N
    
    max_ = max(max_, total - cur)
    cur -= sp[i]
print(max_)
