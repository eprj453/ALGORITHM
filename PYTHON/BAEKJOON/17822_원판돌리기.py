n, m, t = map(int, input().split())
disks = [[]]
for _ in range(n):
    disks.append(list(map(int, input().split())))
rotates = [list(map(int, input().split())) for _ in range(t)]

for rotate in rotates:
    x, d, k = rotate[0], rotate[1], rotate[2]
    for i in range(x, 50, x):
        if i > n:
            break
        else:
            for j in range(k):
                if d == 0:
                    disks[i].insert(0, disks[i].pop())
                elif d == 1:
                    disks[i].append(disks[i].pop(0))


    # i = 0
    # while i <= 50:
    #     if i > n:
    #         break
    #     for
    #     i += 1
# print(disks)
print(rotates)