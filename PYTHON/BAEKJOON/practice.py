# temp = '0001101'
# count = [1]
# for t in range(len(temp)-1):
#     if temp[t] == temp[t+1]:
#         count[-1] += 1
#     else:
#         count.append(1)
#
# print(count)
# # #
# # a = '13'
# # b = '23'
# # print(a+b)
# list1 = [9,6,3,3]
# min_val = min(list1)
# print(min_val)
# # list1[1] = round(list1[1] / 2)
# # print(list1[1] == 4)
# # print(list1)
# # for i in range(len(list1)):
# #     list1[i] = round(list1[i] / 2)
# # print(list1)
# result = False
# while result == False:
#     if result == True:
#         break
#     for i in range(len(list1)):
#         if list1[i] == 1:
#             result = True
#             break
#     if result == False:
#         for i in range(len(list1)):
#             list1[i] = round(list1[i] // min_val)
# #
# print(list1)
# # print(list1)
# #
# my_dict = {'0': [3, 2, 1, 1], '1': [2, 2, 2, 1], '2': [2, 2, 1, 2], '3': [1, 4, 1, 1], '4': [1, 1, 3 ,2],
#            '5': [1, 2, 3, 1], '6': [1, 1, 1, 4], '7': [1, 3, 1, 2], '8': [1, 2, 1, 3], '9': [3, 1, 1, 2]
#            }
#
# print(my_dict.get('10'))
# my_dict = {'3221': 0, '2221': 1, '2212': 2, '1411': 3, '1132': 4,
#            '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9
#             }
# # my_dict = {[3, 2, 1, 1]: 0, [2, 2, 2, 1]: 1, [2, 2, 1, 2]: 2, [1, 4, 1, 1]: 3, [1, 1, 3 ,2]: 4,
# #            [1, 2, 3, 1]: 5, [1, 1, 1, 4]: 6, [1, 3, 1, 2]: 7, [1, 2, 1, 3]: 8, [3, 1, 1, 2]: 9
# #             }
# # print(my_dict.keys())
# # print(my_dict['3221'])
#
# my_dict2 = {'0': '0001101', '1': '0011001', '2': '0010011', '3': '0111101', '4': '0100011',
#            '5': '0110001', '6': '0101111', '7': '0111011', '8': '0110111', '9': '0001011'
#             }

# print(my_dict['0'])
# print([1,2,3,1] in my_dict.values())
# a = 2
# b = 4
# list1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# list2 = [9, 10, 11, 12]
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if list1[i][j] == 3:
#             list1[i].pop(j)
#             c = j
#             for k in range(len(list2)):
#                 list1[i].insert(c, list2[k])
#                 c += 1
#         print(list1[i][j])
# print(list1)


# list1 = [['0', '1', '1234'], ['3', '45', '6']]
# d = {'0': '1234'}
#
# for i in range(len(list1)-1, -1, -1):
#     for j in range(len(list1[i])-1, -1, -1):
#         for k in range(len(list1[i][j])-1, -1, -1):
#             print(list1[i][j][k])
#
# list1 = [0]
# if list1:
#     print(True)

# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         print(list1[i][j])
#         if i == 1 and j == 1:
#             break

# def perm(start, k):
#
#     if start == t:
#         print(temp)
#         return
#
#     for i in range(start, k):
#         temp[start] = list1[i]
#         perm(start+1, k)
#
#
# def perm(n):
#     if n == num:
#         print(temp)
#         return
#     for i in range(num):
#         if compare[i] == i:
#             continue
#         else:
#             t = compare.pop(i)
#             temp[n] = t
#             perm(n+1)
#             compare.insert(t, t)

    # if c == len(list1):
    #     print(temp)
    #     return
    # for i in range(0, e):
    #     print('c, i, list1[c][i] : ', c, i , list1[c][i])
    #     if list1[c][i] == c or i in temp:
    #         continue
    #     else:
    #         temp[s] = list1[c][i]
    #         compare.append(list1[c][i])
    #         search(s+1, e, c+1)
#
#

# arr = [0, 1, 2, 3, 4]
# n = len(arr)
# temp = [0] * n
# visited = [False] * n
#
# def search(s, e):
#     global ans
#     if s == e:
#         print(temp)
#         min_sum = 0
#         for i in range(n):
#             min_sum += arr[temp[i]]
#         ans = min(ans, min_sum)
#         return
#
#     else:
#         for i in range(n):
#             if visited[i]: continue
#             else:
#                 temp[s] = arr[i]
#                 print('i : ', i, end=' ')
#                 print('s :' , s)
#                 visited[i] = True
#                 search(s+1, e)
#                 visited[i] = False
#

# print(13/100)

# def perm(start, end):
# #     if start == end:
# #         print(temp)
# #     else:
# #         for i in range(n):
# #
# #             visited[i] = True
# #             perm(start+1, end)
# #             visited[i] = False
# #
# #
# #
# # list1 = [1, 2, 3, 4]
# # n = len(list1)
# # temp = [0] * n
# # visited = [False] * n
# #
# # perm(0, n)

# list1 = [[1,2],[3,4]]
# if [1,2] in list1:
#     print(True)



# def perm(s, e):
#     global count
#     if s == len(temp):
#         print(temp)
#         count += 1
#         return
#     else:
#         for i in range(n):
#             if visited[i]: continue
#             else:
#                 temp[s] = arr[i]
#                 visited[i] = True
#                 perm(s+1, e)
#                 visited[i] = False
#
#
#
# arr = list(range(100))
# visited = [False]*100
# n = 100
# temp = [0]*10
# count = 0
# perm(0,n)
# # count = 0
# print(count)


# visited_a, visited_b = [], []
# for i in range(3):
#     temp = [False] * 2
#     visited_a.append(temp)
#     visited_b.append(temp)
#
# visited_a[1][1] = True
#
# print(visited_a)
# print(visited_b)


# print(m)
# print(m_1)
# print(remain_2)
# print(c2)
# print()
# print(m_2)
# print(remain_3)
# print(c3)


# def perm(s, e):
#     global count
#     global p_list2
#     if s == e:
#         t = int(''.join(map(str, temp)))
#         p_list2.append(t)
#         return
#     else:
#         for i in range(len(p_list)):
#             if visited[i]:
#                 continue
#             else:
#                 temp[s] = p_list[i]
#                 visited[i] = True
#                 perm(s+1, e)
#                 visited[i] = False
#
#
# p_list = list(map(int, input().split()))
# c = int(input())
# n = len(p_list)
# count = 0
# temp = [0] * n
# visited = [False] * n
# p_list2 = []
# perm(0, n)
# p_list2.sort()
# print(p_list2)
# print(p_list2[c-1])

# c = int(input())
# seats = input().split()
# max_count = 0
# for s in range(len(seats)):
#     if seats[s] == '1': continue
#     else:
#         c1 = 1
#         while 0 <= s-c1 < c:
#             if seats[s-c1] == '1':
#                 break
#             c1 += 1
#         c2 = 1
#         while 0 <= s+c2 < c:
#             if seats[s+c2] == '1':
#                 break
#             c2 += 1
#         t = min(c1, c2)
#         max_count = max(t, max_count)
# print(max_count)

'''
9
1 0 0 0 0 1 1 0 0

'''
# def find(m_x, m_y, c):
#     print('돈다')
#     global count
#     global min_distance
#     if m_x == cony[0] and m_y == cony[1]:
#         count += 1
#         min_distance = c
#         return
#     if m_x > cony[0] or m_y > cony[1]:
#         return
#     for i in range(len(dx)):
#         # if m_x > cony[0] or m_y > cony[1]: continue
#         if 0 <= m_x+dx[i] < paper[1]+1 and 0 <= m_y+dy[i] < paper[0]+1:
#             if visited[m_x+dx[i]][m_y+dy[i]] : continue
#             else:
#                 visited[m_x+dx[i]][m_y+dy[i]] = True
#                 print('m_x+dx[i], my_dy[i]', m_x + dx[i], m_y + dy[i])
#                 find(m_x+dx[i], m_y+dy[i], c+1)
#                 visited[m_x+dx[i]][m_y+dy[i]] = False
#
#
# paper = list(map(int, input().split()))
# cony = list(map(int, input().split()))
# dx, dy = [0, 1], [1, 0]
# visited = []
# for j in range(paper[1]+1):
#     temp = [False] * (paper[0]+1)
#     visited.append(temp)
# print(visited)
# count = 0
# min_distance = 0
# visited[0][0] = True
# find(0, 0, 0)
# # if count == 0 or min_distance == 0:
# #     print('fail')
# # else:
# print(count)
# print(min_distance)

list1 = [[2,3,4,5,6,7,8],[9,10,11,12,13,14,15], [16,17,18,19,20,21,22]]
n = list1[len(list1)-1]
s = 0
while True:
    tmp = len(list1) if s == 0 else 0 if s == 1 else
    for i in range(len(list1)-1, -1, -1):
        if i == 0:
            list1[i] = 0
            break
        list1[i] = list1[i-1]

print(list1)
print(n)
