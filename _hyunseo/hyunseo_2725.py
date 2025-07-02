import math
import time

C = int(input())

def oiler_tocent(n) :
    result = n
    t= 2
    while t * t <= n :
        if n % t == 0 :
            while n % t == 0 :
                n //= t
            result -= result //t
        t += 1
    
    if n > 1 :
        result -= result//n
    return result
        
        

for c in range(C) :
    N = int(input())
    total = 0
    for y in range(2, N+1) :
        total += oiler_tocent(y)
    print(3+2*total)

