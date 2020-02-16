def mirrorPrint(status, mirror):
    s1, e1, g1 = 0, len(mirror), 1
    s2, e2, g2 = 0, len(mirror), 1
    if status == 2:
        s2, e2, g2 = len(mirror)-1, -1, -1
    elif status == 3:
        s1, e1, g1 = len(mirror)-1, -1, -1

    for i in range(s1, e1, g1):
        for j in range(s2, e2, g2):
            print(mirror[i][j], end="")
        print()

n = int(input())
mirror = [input() for _ in range(n)]
k = int(input())
mirrorPrint(k, mirror)



