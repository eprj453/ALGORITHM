n = int(input())
sche = []
can_sche = []
stack = []
for i in range(n):
    sche.append(list(map(int, input().split())))


for i in range(n):
    if sche[i][0] + i > n:
        continue
    else:
        stack.append(sche[i])
        

