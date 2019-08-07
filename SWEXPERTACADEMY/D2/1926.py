# t를 입력하면 1부터 t까지 369게임을 출력해보자
# 박수가 1번이면 -, 2번이면 --를 출력하고 한 칸씩 떨어지게 출력하면 된다
# t = input()
# list1 = []
# list2 = []
# list3 = []
# for i in range(int(t)+1):
#     list1.append(list(str(i)))
#     list2.append(list1[i])
# for j in range(len(list2)):
#     count = 0
#     for k in range(len(list2[j])):
#         if '3' in list2[j][k]:
#             count+=1
#         if '6' in list2[j][k]:
#             count+=1
#         if '9' in list2[j][k]:
#             count+=1
#         list3.append('-'*count)
# print(list3)
        

# t = input()
# list1 = []
# list2 = []
# for i in range(int(t)+1):
#     list1.append(str(i))
# for j in range(len(list1)):
#     count = 0
#     list1[j] = list1[j].replace('3','-')
#     count+=1
#     list1[j] = list1[j].replace('6','-')
#     count+=1
#     list1[j] = list1[j].replace('9','-')
#     count+=1
#     if '-' in list1[j]:
#         list1[j] = '-'*count
#     list2.append(list1[j])
# print(list2)

t = int(input())
list1 = []
list2 = []
for i in range(1,t+1):
    list1.append(str(i))
for j in range(len(list1)):
    if '3' in list1[j]:
        list1[j] = list1[j].replace('3','-')
    if '6' in list1[j]:
        list1[j] = list1[j].replace('6','-')
    if '9' in list1[j]:
        list1[j] = list1[j].replace('9','-')
    count = 0
    if '-' in list1[j]:
        for k in range(len(list1[j])):
            if '-' in list1[j][k]:
                count+=1
        list1[j] = '-'*count
        list2.append(list1[j])
    else:
        list2.append(list1[j])
    print(list2[j], end=' ')
