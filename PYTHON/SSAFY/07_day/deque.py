from collections import deque
import time

start = time.time()

s = deque()
n = 1000000
for i in range(n):
    s.append(i)

while s: # s에서 더 이상 나올 자료가 없을때
    s.pop()

print('실행시간 : {}초'.format(time.time() - start))