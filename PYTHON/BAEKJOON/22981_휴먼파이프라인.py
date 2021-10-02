n, k = list(map(int, input().split()))
speeds = list(map(int, input().split()))
speeds.sort()

max_v = 0

left, right = speeds[0], speeds[1]
left_len, right_len = 1, n-1
for i in range(1, n):
    right = speeds[i]
    left_sum, right_sum = left * left_len, right * right_len
    max_v = max(max_v, left_sum + right_sum)
    left_len += 1
    right_len -= 1

answer = k // max_v if not k % max_v else (k // max_v) + 1
print(answer)
