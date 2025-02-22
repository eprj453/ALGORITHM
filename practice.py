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


# url = 'http://apis.data.go.kr/1611000/DceDgnssIdxService/getIdxOparea?'
#
# serviceKey = '58vxMI8sB6fw8%2BIjFlgpquKMFDNff69sl%2FA0wHlskhx7O3NS1ElZEGW7FWOwshgtLdQlRYhKP%2BW6FHWKi%2Bg7oQ%3D%3D'
#
# cd = pd.read_csv('bnd_oa_bnd_oa_3901.csv', engine='python')
# idx_codes = pd.read_excel('bnd_oa_bnd_oa_39_idxcd.xlsx')
#
# column_name = {
#     'SIGNGU_CODE': 'signguCd',
#     'EMD_CODE': 'emdCd',
#     'OPAREA_CODE': 'opareaCd'
# }
#
# url += f'&serviceKey={serviceKey}'
#
# columns = ['emdCd', 'emdNm', 'opareaCd', 'idxCd', 'year', 'idxMean', 'value', 'valueCd']
#
# for year in ['2015']:
#     df = pd.DataFrame(columns=columns)
#     df.to_csv(f'{year}.csv', mode='w', header=None)
#     url += f'&year={year}'
#     year_cut = len(url)
#     for i in range(cd.shape[0]):
#         cd_row = cd.loc[i]
#         cd_cut = len(url)
#         for code in column_name.keys():
#             key = column_name.get(code)
#             url += f'&{key}={int(cd_row.get(code))}'
#         idx_cut = len(url)
#         for j in range(idx_codes.shape[0]):
#             idx_row = idx_codes.loc[j]
#             idx_code = idx_row.get('지표코드')
#             url += f'&idxCd={idx_code}'
#             response = requests.get(url).json()
#             if response.get('header').get('resultCode') == '00':
#                 body = response.get('body')
#                 append_row = []
#                 for c in columns:
#                     append_row.append(body.get(c, ''))
#                 write_row = pd.DataFrame([append_row])
#             else:
#                 write_row = pd.DataFrame(
#                     [['', '', cd_row.get('EMD_CODE'), cd_row.get('EMD_NM'), cd_row.get('OPAREA_CODE'), '', '', '']])
#             write_row.to_csv(f'{year}.csv', mode='a', header=None)
#
#             url = url[:idx_cut]
#         url = url[:cd_cut]
#     url = url[:year_cut]

# def index_2d(arr, ele, n):
#     pos = [0, 0]
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == ele:
#                 return [i, j]
#     return pos
#
# def find_shortest_way(start, end, n):
#     start_x, start_y = start
#     end_x, end_y = end
#
#     shortest_x = min(abs(start_x - end_x), (start_x + (n-1 - end_x) + 1), (end_x + (n-1 - start_x) + 1))
#     shortest_y = min(abs(start_y - end_y), (start_y + (n-1 - end_y) + 1), (end_y + (n-1 - start_y) + 1))
#
#     return shortest_x + shortest_y + 1# 가장 짧게 이동한 x 거리 + 가장 짧게 이동한 y 거리 + enter
#
# def solution(n, board):
#     answer = 0
#     start = [0, 0]
#     erase_numbers = list(range(1, (n**2)+1))
#     for num in erase_numbers:
#         next_number_index = index_2d(board, num, n)
#         answer += find_shortest_way(start, next_number_index, n)
#         start = next_number_index
#
#     return answer
#
#
#
# arr = [[3, 5, 6],
#        [9, 2, 7],
#        [4, 1, 8]]
#
# arr2 = [[11, 9, 8, 12],
#         [2, 15, 4, 14],
#         [1, 10, 16, 3],
#         [13, 7, 5, 6]]
# arr3 = [[2, 3], [4, 1]]
# print(solution(2, arr3))
#
# logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80"," 0002 5 100", "0003 99 90"]
#
# for log in logs:
#     stu_num, test_num, grade = log.split()
#     print(stu_num, test_num, grade)

from itertools import permutations


def is_less_than_number(arr, num):
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) > num:
            return False
    return True

def count_difference(arr1, arr2):
    cnt = 0

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            cnt += 1

    return cnt

arr = [3, 7, 2, 8, 6, 4, 5, 1]
n = 3
all_arr = list(permutations(arr, len(arr)))

possible_arr = []
for a in all_arr:
    if is_less_than_number(a, n):
        possible_arr.append(a)

min_count_arr = []
cnt = len(arr)
for a in possible_arr:
    diff_cnt = count_difference(arr, a)
    if diff_cnt < cnt:
        min_count_arr = [a]
        cnt = diff_cnt
    elif diff_cnt == cnt:
        min_count_arr.append(a)



print(cnt)
print(min_count_arr)

# for arr in all_list:
'''
[1, 2, 3, 4, 5, 6 ,7, 8]
[3, 5, 7, 6, 1, 2, 8, 4]

[3, 2, 1, 4, 5, 6 ,7, 8]


'''



'''
[10, 20, 30, 40, 50]

'''

