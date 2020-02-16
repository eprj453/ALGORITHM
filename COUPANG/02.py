import time


def subset(arr, k, t):

    ans = 0
    # print(1 << len(arr))
    for i in range(0, 1 << len(arr)):
        s, count = 0, 0
        for j in range(0, len(arr)):
            if i & (1 << j):
                s += arr[j]
                count += 1
        # print(s, count)
        if count >= k and s <= t:
            ans += 1
    return ans


def solution(arr, k, t):
    start = time.time()
    answer = subset(arr, k, t)
    print(time.time() - start)
    return answer
print(solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 7, 30))