from queue import Queue

def solution(n, path, order):
    answer = True
    trees = [[] for _ in range(n)]
    targeting = [None] * (n)
    be_targeted = [None] * (n)
    visited = [False] * (n)

    for v, w in path:
        trees[v].append(w)
        trees[w].append(v)
    for v, w in order:
        targeting[v] = w
        be_targeted[w] = v

    parents = [None] * n

    parent_queue = Queue()
    parent_queue.put(0)

    while not parent_queue.empty():
        node = parent_queue.get()
        print("node : ", node)
        for no in trees[node]:
            print("no : ", no)
            if no and parents[no] == None:
                parents[no] = node
                parent_queue.put(no)
    print(trees)
    print(parents)

    stk = [0]

    cnt = 0
    while stk:
        node = stk.pop()

        if be_targeted[node] and not visited[be_targeted[node]]: continue

        visited[node] = True

        if targeting[node]:
            p = parents[targeting[node]]
            if visited[p]:
                target = targeting[node]
                stk.append(target)

        for no in trees[node]:
            if not visited[no]:
                stk.append(no)


    print(visited)
    print(cnt == n)
    return all(visited)

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[4,1],[8,5],[6,7]]))