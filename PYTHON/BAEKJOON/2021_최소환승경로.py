# import heapq

# from collections import namedtuple
# from pprint import pprint

# N, L = list(map(int, input().split(' ')))

# connected_lines = [[] for _ in range(N+1)]
# connected_stations = [[] for _ in range(N+1)]
# Station = namedtuple('Station', ['station', 'line'])

# for i in range(1, L+1):
#     lines = list(map(int, input().split(' ')))
#     for j in range(len(lines)-1):
#         s, next_s = lines[j], lines[j+1]
#         connected_lines[s].append(i)
#         if next_s == -1: break

#         connected_stations[s].append(Station(station=next_s, line=i))

#         if j >= 1:
#             before_s = lines[j-1]
#             connected_stations[s].append(Station(station=before_s, line=i))





# start, end = list(map(int, input().split(' ')))
# answer = -1

# visited = [False] * (N+1)
# visited[start] = True

# hq = []

# for line in connected_lines[start]:
#     heapq.heappush(hq, [0, start, line])

# while hq:
#     transfer_count, current_station, current_line = heapq.heappop(hq)

#     for connected_station in connected_stations[current_station]:
#         next_station, next_line = connected_station.station, connected_station.line

#         if next_station == end:
#             answer = max(transfer_count, answer) if next_line == current_line else max(transfer_count + 1, answer)
#             break

#         elif not visited[next_station]:
#             if next_line != current_line:
#                 next_station_info = [transfer_count+1, next_station, next_line]
#             else:
#                 next_station_info = [transfer_count, next_station, current_line]
#             heapq.heappush(hq, next_station_info)
#             visited[next_station] = True

for i in range(5):
    print(i)
else:
    print('aaa')