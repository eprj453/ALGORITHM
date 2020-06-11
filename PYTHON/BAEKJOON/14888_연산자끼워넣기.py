# max_val = -(10 ** 9)
# min_val = 10 ** 9
#
# def operation(ans, nums, p, mi, mul, di, idx):
#     global max_val, min_val
#     if not (p + mi + mul + di):
#         print(ans)
#         max_val = max(ans, max_val)
#         min_val = min(ans, min_val)
#         return
#
#     if p:
#         operation(ans + nums[idx], nums, p-1, mi, mul, di, idx+1)
#     if mi:
#         operation(ans - nums[idx], nums, p, mi-1, mul, di, idx+1)
#     if mul:
#         operation(ans * nums[idx], nums, p, mi, mul-1, di, idx+1)
#     if di:
#         operation(ans // nums[idx], nums, p, mi, mul, di-1, idx+1)
#
#
# n = int(input())
# nums = list(map(int, input().split()))
# p, mi, mul, di = map(int, input().split())
# operation(nums[0], nums, p, mi, mul, di, 1)
# print(max_val, min_val)

print(list('hello'))