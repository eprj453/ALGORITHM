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

class SSN:
    def __init__(self, data):
        if not isinstance(data, str):
            raise TypeError("문자열이 아닙니다.")
        elif not (data[0:6].isdigit() or data[6] == "-" and data[7:].isdigit()):
            raise TypeError("주민등록번호 양식이 아닙니다.")
        elif len(data) != 14:
            raise TypeError("14자의 길이가 아닙니다")
        self.data = data

    def birthday(self):
        import datetime
        if self.data[7] in ['1', '2', '5', '6']:
            year = 1900 + int(self.data[0:2])
        elif self.data[7] in ['3', '4', '7', '8']:
            year = 2000 + int(self.data[0:2])
        else:
            year = 1800 + int(self.data[0:2])
        month = int(self.data[2:4])
        day = int(self.data[4:6])
        return datetime.date(year, month, day)

    def gender(self):
        import datetime
        if int(self.data[7] in ['1', '3', '5', '7', '9']):
            gender = True
        else:
            gender = False
        return gender

    def age(self):
        import datetime
        today = int(datetime.date.today().strftime("%Y%m%d"))
        birthday = int(self.birthday().strftime("%Y%m%d"))
        age = (today - birthday) // 10000
        return age


datas = ["920515-1133555", "871209-2233777", "080209-4455666"]
for data in datas:
    obj = SSN(data)
    print(f"생년월일: {obj.birthday()}")
    print(f"만나이: {obj.age()}")
    if obj.gender():
        print("성별:남")
    else:
        print("성별:여")