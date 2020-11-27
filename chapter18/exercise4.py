from collections import deque

def search(G, s, v):
    parent_pointers = {s : None}
    q = deque()
    q.append(s)
    while len(q) != 0:
        curr = q.popleft()
        for w in G[curr]:
            if w not in parent_pointers:
                parent_pointers[w] = curr
                q.append(w)
    result = []
    if v in parent_pointers:
        iterator = v
        while iterator is not None:
            result.append(iterator)
            iterator = parent_pointers[iterator]
    return result[::-1]
