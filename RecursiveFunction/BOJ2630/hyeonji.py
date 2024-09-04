import sys
input = sys.stdin.readline

def algo(x,y,num):
    global w,b
    color = arr[y][x]
    val=num//2
    for i in range(y,y+num):
        for j in range(x,x+num):
            if color != arr[i][j]:
                algo(x,y,val)
                algo(x+val,y,val)
                algo(x,y+val,val)
                algo(x+val,y+val,val)
                return
    if color:
        b+=1
    else:
        w+=1

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]

w,b=0,0
algo(0,0,n)
print(w)
print(b)