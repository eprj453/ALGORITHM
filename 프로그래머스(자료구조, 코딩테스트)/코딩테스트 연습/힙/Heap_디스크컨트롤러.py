import heapq


def solution(jobs):
    answer = 0
    jobs.sort()
    heapq.heapify(jobs)
    controller = None

    while jobs:
        job = heapq.heappop(jobs)

        if controller is None:
            controller = job
        else:


    return answer


solution([[0, 3], [1, 9], [2, 6]])