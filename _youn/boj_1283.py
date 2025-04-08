N = int(input())
shortkey = {}
words = []

for _ in range(N):
    word = input()
    findKey = False

    for w in word.split():
        key = w[0].lower()
        if not key: continue 
        if key not in shortkey:
            shortkey[key] = True
            word = word.replace(w, f"[{w[0]}]{w[1:]}", 1)
            findKey = True
            break
    
    if not findKey:
        for i, w in enumerate(word):
            key = w.lower()
            if key not in shortkey and w!=' ':
                shortkey[key] = True
                word = word[:i] + f"[{word[i]}]" + word[i+1:]
                break

    words.append(word)
print(*words, sep='\n')