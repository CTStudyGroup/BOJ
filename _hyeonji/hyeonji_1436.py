import sys
input=sys.stdin.readline

n=int(input())
name=666

while 1:
    if '666' in str(name):
        n-=1
        if n==0:
            break
    name+=1

print(name)