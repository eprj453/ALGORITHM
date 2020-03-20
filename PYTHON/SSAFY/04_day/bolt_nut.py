import sys
sys.stdin = open('bolt_input.txt', 'r')

t = int(input())

for i in range(1, t+1):
    n = int(input())
    bolt_list = list(map(int, input().split()))
    bolt_list2 = []
    bolt_list3 = []
    nut_list = []
    answer = ''

    for j in range(0 ,n*2, 2):
        bolt_list2.append([bolt_list[j], bolt_list[j+1]])
        nut_list.append(bolt_list[j+1])

    for j in range(len(bolt_list2)):
        temp = bolt_list2[j]
        for k in range(len(bolt_list2)):
            if temp[0] not in nut_list:
                bolt_list3.append(temp)
                break

    while len(bolt_list3) < len(bolt_list2):
        for val in bolt_list2:
            if bolt_list3[-1][1] == val[0]:
                bolt_list3.append(val)

    for j in range(len(bolt_list3)):
        for k in range(0, 2):
            if k == 1 and j == len(bolt_list3)-1:
                answer += str(bolt_list3[j][k])
            else:
                answer += str(bolt_list3[j][k])+' '

    print('#{} {}'.format(i, answer))


