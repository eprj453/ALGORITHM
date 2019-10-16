
V, E = map(int, input().split())

Edge, MST = [], []
for _ in range(E):
    Edge.append(tuple(map(int, input().split())))

#================================
p = [0] * V
def init():
    for i in range(V):
        p[i] = i

def find(a):
    if p[a] == a: return a
    p[a] = find(p[a])
    return p[a]

#================================

Edge.sort(key=lambda x: x[2])
init()
cnt, cur = V - 1, 0
while cnt:
    u, v, w = Edge[cur]
    a, b = find(u), find(v)
    if a != b:
        p[a] = b
        MST.append((u, v, w))
        cnt -= 1
    cur += 1

for edge in MST:
    print(edge)
