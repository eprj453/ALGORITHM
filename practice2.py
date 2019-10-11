import time

# print((5+1)%6 + (4+1)%6)


# n = 4 # 배열 크기
# m = 9
# print('몫 : ',n//m)
# print('나머지 : ',n%m)
# 현재 인덱스 1
# 총 이동 횟수 8
# 제한 칸 6

# (r - (s - x)) // r
# for i in range(1, 30): # 감소로 시작
#     n = (10 + (i-6)) // 10 # 몫
#     m = (10 + (i-6)) % 10
#     if n % 2:
#         print(n)
#         print(m)
#     else:
#         print(n)
#         print(10 - m)
#     print()
# print('change')
#
# for i in range(1, 20): # 증가로 시작
#     n = ((i+2) // 7)
#     m = ((i+2) % 7)
#     if n % 2:
#         print(n)
#         print(7-m)
#     else:
#         print(n)
#         print(m)
#     print()

# print(9//5)
# print(9%5)
#
# list1 = [0,1,2,3,4,5]
# ans = {0,1,2,3,4,5}
# n, c = 0, 5
#
# for j in list(ans):
#     for lis in list1:
#         if int((str(lis) + str(j))) == 1111 or int((str(j) + str(lis))) == 1111:
#             print('c')
#         ans.add(int((str(lis) + str(j))))
#         ans.add(int((str(j) + str(lis))))
#     # ans.add(list)
#     # c += 1
# print(len(ans))
# print(ans)
#
# start = time.time()
# set_num = 793881
# n = 1
# c = set_num // 2
# t_list = []
# while n <= c:
#     if set_num % n == 0:
#         t_list.append(n)
#     n += 1
#
# print(t_list)
# print('time : {}'.format(time.time() - start))
#
# list1 = [5,4,3,2,1]
# list1 = list1[2:]
# print(list1)
#
# def comb(s, start):
#     global cnt
#     cnt += 1
#     if s == r:
#         print(temp)
#         return
#
#     else:
#         for i in range(start, n):
#             temp.append(list1[i])
#             comb(s+1, i+1)
#             temp.pop()
#             # if visited[i]: continue
#             # else:
#             #     visited[i] = True
#             #     temp[s] = list1[i]
#             #     comb(s+1)
#             #     visited[i] = False
#
# list1 = list(range(64))
# n = len(list1)
# temp = []
# r = 3
# visited = [False] * n
# cnt = 0
# comb(0, 0)
# print(cnt)

a = '(3+4)*2'
print(int(a))