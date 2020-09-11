# from queue import PriorityQueue
#
#
# def make_bin(string):
#     answer = ''
#     for ch in string:
#         answer += '0' if ch == 'x' else '1'
#     return int(answer, base=2)
#
#
# def dijk(start, end):
#     distance = [0xffff] * 513
#     path = [i for i in range(513)]
#     visited = [False] * 513
#     distance[start] = 0
#
#     pq = PriorityQueue()
#     pq.put((0, start))
#
#     while not pq.empty():
#         dis, unit = pq.get()
#         if dis > distance[unit]: continue
#         visited[unit] = True
#         for v, w in graph[unit]:
#             if not visited[v] and distance[v] > distance[unit] + w:
#                 distance[v] = distance[unit] + w
#                 path[v] = unit
#                 pq.put((distance[v], v))
#
#     return -1 if distance[end] == 0xffff else distance[end]
#
#
# n, k = map(int, input().split())
# graph = [[] for _ in range(513)]
#
# for _ in range(k):
#     f1, f2, cost = input().split()
#     f1, f2 = make_bin(f1), make_bin(f2)
#     # print(f1, f2)
#     graph[f1].append((f2, int(cost)))
#
# q = int(input())
# for _ in range(q):
#     q1, q2 = input().split()
#     q1, q2 = make_bin(q1), make_bin(q2)
#     answer = dijk(q1,q2)
#     print(answer)

# dijk(1, 3)
# n, k = map(int, input().split())
# max_value = 0
# answer = 0.0
# cookies = []
# for _ in range(n):
#     cookie = float(input())
#     max_value += cookie
#     cookies.append(cookie)
# start, end = 0, max_value
#
# while start <= end:
#     cookie_count = 0
#
#     mid = (start + end) / 2
#     for c in cookies:
#         can_make = c // mid
#         cookie_count += can_make
#     print('cookie_count : {}'.format(cookie_count))
#     print('start : {}'.format(start))
#     print('end : {}'.format(end))
#     print('mid : {}'.format(mid))
#     print()
#     if cookie_count == k:
#         answer = mid
#
#     if cookie_count >= k:
#         start = mid + 0.0001
#     else:
#         end = mid - 0.0001
#
# print(answe

print(((1), (2)) == ((2), (1)))