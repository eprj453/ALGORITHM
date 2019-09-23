# n, k = map(int, input().split())
# #
# # q = []
# # q.append([n, 0])
# #
# # while len(q) > 0:
# #     if q[0][0]+1 == k or q[0][0]-1 == k or q[0][0]*2 == k:
# #         print(q[0][1] + 1)
# #         break
# #     else:
# #
# #         q.append([q[0][0]+1, q[0][1]+1])
# #         q.append([q[0][0]-1, q[0][1] + 1])
# #         q.append([q[0][0]*2, q[0][1] + 1])
# #
# #     q.pop(0)


# def find(s, e, count):
#     global ans
#     if s == e:
#         ans = count
#         return
#     else:
#         print(s)
#         find(s-1, e, count+1)
#         find(s+1, e, count+1)
#         find(s*2, e, count+1)
#
# n, k = map(int, input().split())
# ans = 0
# find(n, k, 0)
# print(ans)

n, m = 5, 78
remain_1, remain_2, remain_3 = 0, 0, 0
c, c2, c3 = 0, 0, 0
count = 0
if m % 2 == 0: # 짝수 경우
    while m >= n:
        if n - (m // 2) > m - n:
            break
        if m % 2 == 1:
            remain_1 += 1
        m //= 2
        c += 1
    print(m)
    print(c)
    print(remain_1)
else:
    m_1, m_2 = m-1, m+1
    while m_1 >= n:
        if n - (m_1 // 2) > m_1 - n:
            break
        if m_1 % 2 == 1:
            remain_2 += 1
        m_1 //= 2
        c2 += 1
    while m_2 >= n:
        if n - (m_2 // 2) > m_2 - n:
            break
        if m_2 % 2 == 1:
            remain_3 += 1
        m_2 //= 2
        c3 += 1