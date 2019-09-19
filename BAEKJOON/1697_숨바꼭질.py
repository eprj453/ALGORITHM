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


def find(s, e, count):
    global ans
    if s == e:
        ans = count
        return
    else:
        print(s)
        find(s-1, e, count+1)
        find(s+1, e, count+1)
        find(s*2, e, count+1)

n, k = map(int, input().split())
ans = 0
find(n, k, 0)
print(ans)