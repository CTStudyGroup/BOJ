def zoac(word, start, end, visited):
    if start >= end: # base condition
        return
    
    min_c = '['
    min_idx = -1
    for i in range(start, end):
        if not visited[i] and word[i] < min_c:
            min_c = word[i]
            min_idx = i
    visited[min_idx] = True

    print(''.join([word[i] for i in range(len(word)) if visited[i]]))
    zoac(word, min_idx+1, end, visited)
    zoac(word, start, min_idx, visited)

word = input().strip()
visited = [False]*len(word)
zoac(word, 0, len(word), visited)