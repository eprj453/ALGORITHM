import sys
sys.stdin = open('1952_input.txt', 'r')

# 메모이제이션


n = 1
for i in range(1, 10):
    n *= i
    # print(i)
print(n * (2**9))


