# input_ = input()
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**3)

# 원자량 저장
dic={}
dic["H"] = 1
dic["C"] = 12
dic["O"] = 16

        
def recurs(start) :
    idx = start
    total = 0
    while idx < len(S) :
      # 문장의 끝 도달
        if idx >= len(S)-1 :
            return idx, total
        # 새로운 괄호를 만나게 된다면, 재귀 시작
        if S[idx] == "(" :
            idx, tmp = recurs(idx+1)
            total += tmp
            continue
        # 닫는 괄호를 만나게 된다면,뒤에 숫자가 있는 경우는 곱한 후 반환
        if S[idx] == ")" :
            if idx < len(S)-1 and S[idx+1].isdigit():
                return idx + 2, total * int(S[idx+1])
            else :
                return idx + 1, total
        # 원자 만나는 경우, 원자 다음이 숫자이면 곱함
        if S[idx] == "C" or S[idx] == "H" or S[idx] == "O" :
            if S[idx + 1].isdigit() :
                total += (dic[S[idx]] * int(S[idx + 1]) )
                idx += 2
                
            else :
                total += (dic[S[idx]])
                idx += 1
    

S = input()
print(recurs(0)[1])
