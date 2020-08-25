# 5 8 3
# 2 4 5 4 6
# answer -> 46
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

# 풀이 1
# k_count = 0
# for i in range(m, 0, -1):
#     if k_count == k:
#         answer += arr[-2]
#         k_count = 0
#     else:
#         answer += arr[-1]
#         k_count += 1
# 시간초과 날 수 있음(m이 엄청나게 클 경우)

cnt = k+1
answer += (arr[-2] * (m//cnt)) # 2번째로 큰 수는 몫만큼 더할수 있다.
answer += (arr[-1] * (((m//cnt) * k) + m % cnt))
print(answer)
