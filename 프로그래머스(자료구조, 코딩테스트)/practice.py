from queue import PriorityQueue

def solution(subway, start, end):
    stations = [[] for _ in range(200001)]
    lines = [[] for _ in range(1000001)]

    for i in range(len(subway)):
        line = i
        subw = subway[i].split(" ")
        for j in range(len(subw)-1):
            current_station, next_station = int(subw[j]), int(subw[j+1])
            stations[current_station].append((next_station, line))
            lines[line].append(current_station)
    print(stations[:20])
    answer = 0
    return answer


solution(["1 2 3 4 5 6 7 8", "2 11", "0 11 10", "3 17 19 12 13 9 14 15 10", "20 2 21"], 1, 9)