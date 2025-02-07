N = int(input())

arr = list(input() for _ in range(N))

arr.sort()
words = []  # 접두사X 집합

for new_word in arr:
    for word in words:
        if new_word.find(word) == 0:  # 추가하고자 하는 단어가 word로 시작하는 경우
            words.remove(word)  # 기존 word를 리스트에서 제거
    words.append(new_word)  # 새로운 단어를 접두사X 집합에 추가

print(len(words))
