G = int(input())

i, j = 1, 2
flag = True

while i < j:
    diff = j*j - i*i
    
    if diff == G:
        print(j)
        flag = False
        j += 1
    elif diff < G:
        j += 1
    else:
        i += 1

if flag:
    print(-1)
