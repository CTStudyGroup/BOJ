n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

answer=[]
if len(a)==0 or len(b)==0:
    print(len(answer))
else:
    # print(set(a)&set(b))
    part=set(a)&set(b)
    while part:
        max_part=max(part)
        a_idx=a.index(max_part)
        b_idx=b.index(max_part)

        answer.append(max_part)

        a=a[a_idx+1:]
        b=b[b_idx+1:]

        part=set(a)&set(b)

print(len(answer))
print(*answer)