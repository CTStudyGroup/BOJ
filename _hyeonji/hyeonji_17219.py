import sys
input=sys.stdin.readline

n,m=map(int,input().split())

info=dict()
for i in range(n):
    address,password=input().split()
    info[address]=password

for i in range(m):
    address_=input().rstrip()
    print(info[address_])