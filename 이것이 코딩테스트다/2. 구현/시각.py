n = int(input())
h, m, s = 0, 0, 0
answer = 0
while h <= n:
    time = str(h) + str(m) + str(s)
    if '3' in time:
        answer += 1
    s += 1
    if s > 59:
        s = 0
        m += 1
    if m > 59:
        h += 1
        m = 0
        s = 0
    print(h, m, s)
print(answer)