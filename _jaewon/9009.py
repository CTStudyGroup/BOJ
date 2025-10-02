T = int(input())

pibo = []
pibo.append(0)
pibo.append(1)

new = 1
index = 2
while True:
    new = pibo[index-1] + pibo[index-2]

    if(new > 1000000000):
        break

    pibo.append(new)
    index += 1


for _ in range(T):
    target = int(input())

    tmp = target
    result = []
    while tmp != 0:
        
        maximum_index = 0
        for index in range(len(pibo)-1, 0, -1):
            if(pibo[index] <= tmp):
                maximum_index = index
                break
        
        tmp -= pibo[maximum_index]
        result.append(pibo[maximum_index])
    
    result.sort()
    print(*result)