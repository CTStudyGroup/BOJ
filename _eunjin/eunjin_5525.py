N = int(input())
M = int(input())
string = input()

# 시간 초과 풀이
# search = "IO"*N+"I"

# curr_string = string
# cnt = 0
# while(True):
#     idx = curr_string.find(search)
#     if idx == -1:  # 현재 문자열에 IOI가 없는 경우
#         break

#     cnt += 1
#     curr_string = curr_string[idx+1:]

# print(cnt)

patterns = []
idx = string.find("IOI")
if idx == -1:
    print(0)
    exit()

cnt = 0
while(idx <= M-2):
    # print("idx:", idx)
    if string[idx:idx+3] == "IOI":
        cnt += 1
        idx += 2
    else:
        if cnt > 0:
            patterns.append("IO"*cnt+"I")
            cnt = 0
        idx += 1
    # print("after idx:", idx, ", cnt:", cnt, ", patterns:", patterns)
    # print("==================")

if cnt > 0:
    patterns.append("IO"*cnt+"I")

answer = 0
for pattern in patterns:
    if len(pattern) < 2*N+1:
        continue
    elif len(pattern) == 2*N+1:
        answer += 1
    else:
        answer += 1
        answer += (len(pattern)-1-2*N)//2
        # IOIOIOIOIO , IOIO
        # 10 , 4
        # 1+ 6//2
print(answer)
