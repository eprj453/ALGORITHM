def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start, end = 0, distance
    print(rocks)
    while start <= end:
        mid = (start + end) // 2
        curr_rock = 0
        rock_count = 0
        for idx, rock in enumerate(rocks, start=0):
            if rock - curr_rock < mid:
                rock_count += 1
            else:
                curr_rock = rock

        if rock_count > n:

            end = mid - 1
        else:
            if rock_count == n:
                answer = max(answer, mid)
            start = mid + 1

    return answer


arr = [1, 2, 3, 4, 5]
print([arr[i] if i == 1 else i == 2 for i in range(len(arr))])