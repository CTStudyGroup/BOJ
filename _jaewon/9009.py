T = int(input())

pibo = []
pibo.append(0)
pibo.append(1)

index = 2
new = 1
while new < 1000000000:
    new = pibo[index-1] + pibo[index-2]
    pibo.append(new)
    index += 1

for _ in range(T):
    n = int(input())
    result=[]
    while(n):
        for k in range(46):
            if(pibo[k]<=n):
                t = pibo[k]
        n -= t
        result.append(t)
        result.sort()
        
    for b in range(len(result)):
        print(result[b], end=' ')
