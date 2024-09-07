import sys
input=sys.stdin.readline

def algo(num):
    if num==1:
        return '*'

    star=algo(num//3)
    answer = []

    for i in star:
        answer.append(3*i)
    for i in star:
        answer.append(i+' '*(num//3)+i)
    for i in star:
        answer.append(3*i)
    return answer

n=int(input())
print('\n'.join(algo(n)))