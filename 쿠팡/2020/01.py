# def convert(num, flag):
#     t = "0123456789ABCDEF"
#     q, r = divmod(num, flag)
#
#     if not q:
#         return t[r]
#     return convert(q, flag) + t[r]
#
#
# print(convert(2, 2))
#
# def solution(N):
#     answer = []
#     for i in range(2, 9):
#         result = convert(N, i)
#         tmp = 1
#         for n in str(result):
#             if n != '0':
#                 tmp *= int(n)
#         if not answer or answer[1] <= tmp:
#             answer = [i, tmp]
#         else:
#             if answer[1] <= tmp:
#                 answer = [i, tmp]
#     return answer
#
#
# print(solution(1000000))
#
# c

arr = [1, 2, 3]
print(sorted(arr, key=lambda x:(-x)))