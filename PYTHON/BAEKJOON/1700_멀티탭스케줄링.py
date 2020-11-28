import heapq


def index_from_start(start, arr, n):
    cnt = start
    for i in range(start, len(arr)):
        if arr[i] == n:
            return i
    return len(arr)


n, k = map(int, input().split())
schedules = list(map(int, input().split()))

hq = []
heapq.heapify(hq)
answer = 0

for idx, stuff in enumerate(schedules):
    if
print(answer)
