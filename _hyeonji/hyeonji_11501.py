t=int(input())

for i in range(t):
    n=int(input())
    info=list(map(int,input().split()))

    info.reverse()

    maxx=0
    answer=0
    for j in range(len(info)):
        if info[j]>maxx:
            maxx=info[j]
        else:
            answer+=maxx-info[j]

    print(answer)