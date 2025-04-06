from sys import stdin as s

s = open("txt/2212.txt","r")

N = int(s.readline())
K = int(s.readline())
sensors = list(map(int,s.readline().split()))

sensors.sort()
sub = [(0,0)]
for i in range(1,N):
    sub.append((i,sensors[i]-sensors[i-1]))

sub.sort(key = lambda x : -x[1])
cut = sub[0:K-1] # K보다 작은 수로 컷
cut.sort(key = lambda x : x[0])

print(cut)
result = 0
last_center = 0
for i in range(len(cut)):
    unit = sensors[last_center:cut[i][0]]
    print(unit)
    if len(unit) <= 1: # 길이가 0이라면 수신가능영역 0
        pass
    else:
        result += (unit[-1] - unit[0])
#   print(sensors[last_center:cut[i][0]])
    last_center = cut[i][0]

unit = sensors[last_center:]

result += (unit[-1] - unit[0])
print(result)
# 54m 43s