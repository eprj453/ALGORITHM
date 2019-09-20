for i in range(1, int(input())+1):
    w, h = map(int, input().split())
    start = []
    maps = []
    c = 0
    while c < h:
        temp = list(input())
        if '@' in temp:
            start = [c, temp.index('@')]
            c += 1
        else:
            c += 1
        maps.append(temp)
    print(start)
    print(maps)