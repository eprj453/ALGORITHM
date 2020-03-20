def paper(n):
    if n == 10:
        return 1
    if n == 20:
        return 3
    return paper(n-10) + (paper(n-20) * 2)


t = int(input())
for i in range(1, t+1):
    n = int(input())
    print('#{} {}'.format(i, paper(n)))
print(paper(40))