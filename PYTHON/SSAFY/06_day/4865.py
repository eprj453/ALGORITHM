import sys
sys.stdin = open('4865_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    str1 = set(input())
    str2 = input()
    max_count = 0
    for letter1 in str1:
        count = 0
        for letter2 in str2:
            if letter2 == letter1:
                count += 1
        if count > max_count:
            max_count = count
    print('#{} {}'.format(i, max_count))