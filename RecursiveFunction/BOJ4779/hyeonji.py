import sys
input = sys.stdin.readline

def algo(num):
    if num==1:
        return '-'

    line=algo(num//3)
    return line+' '*(num//3)+line

while 1:
    try:
        n=int(input())
        print(algo(3**n))
    except:
        break