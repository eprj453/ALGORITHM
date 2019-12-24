import sys
sys.stdin = open('4864_input.txt', 'r')

t = int(input())
for i in range(1, t+1):
    str1 = input()
    str2 = input()
    result = 0
    count = 0
    for num2 in range(len(str2)-len(str1)+1):
        for num1 in range(len(str1)):
            if str2[num2+num1] == str1[num1]:
                count += 1
            else:
                count = 0
                break

        if count == len(str1):
            result = 1
            break

    print('#{} {}'.format(i, result))