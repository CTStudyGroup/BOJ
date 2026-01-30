import sys
input = sys.stdin.readline

nums = [0]
for _ in range(6) :
    nums.append(int(input()))
# 꽉 찬 개수
cnt = 0 
# cur[1] = 1*1 들어갈 수 있는 개수
# cur[2] = 2*2 들어갈 수 있는 개수
cur = [0,0, 0]

for n in range(3, 7) :
    if n == 3 :
        cnt += nums[3] // 4
        nums[3] %= 4
        if nums[3] != 0 :
            cnt += 1
        if nums[3] == 1 :
            cur[1] += 7
            cur[2] += 5
        elif nums[3] == 2 :
            cur[1] += 6
            cur[2] += 3
        elif nums[3] == 3 :
            cur[1] += 5
            cur[2] += 1
    if n == 4 :
        cnt += nums[4]
        cur[2] += nums[4]*5
    if n == 5 :
        cnt += nums[5]
        cur[1] += nums[5]*11
    if n == 6 :
        cnt += nums[6]


    print(f'n : {n} cnt : {cnt} cur :{cur}')
        
for n in range(2, 0, -1) :
    if n == 2 :

        if cur[2] < nums[2] :
            nums[2] -= cur[2]
            cur[2] = 0
            cnt += (nums[2] // 9)
            nums[2] %= 9
            if nums[2] != 0 :
                cur[1] += (36 - 4*nums[2])
                cnt += 1
            
        else :
            cur[2] -= nums[2]
    if n == 1 :
        cur[1] += cur[2]*4
        cur[2] = 0
        if cur[1] < nums[1] :
            nums[1] -= cur[1]
            cur[1] = 0

            cnt += ((nums[1] // 36))
            if nums[1] % 36 != 0 :
                cnt += 1
        else :
            cur[1] -= nums[1]

    print(f'n : {n} cnt : {cnt} cur :{cur}')
print(cnt)
