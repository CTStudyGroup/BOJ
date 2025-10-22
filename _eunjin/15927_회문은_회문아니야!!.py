S = input().strip()

if S != S[::-1]:  # 회문이 아니면 문자열 전체 길이 출력
    print(len(S))
elif len(set(S)) == 1:  # 모두 같은 문자라면 -1
    print(-1)
else:  # 회문이지만 모두 같은 문자가 아닐 경우
    print(len(S) - 1)
