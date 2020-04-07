
# 1번
# def solution(inputString):
#     answer = -1
#     inputDict = {
#         '(' : 0,
#         ')' : 0,
#         '{' : 0,
#         '}' : 0,
#         '[' : 0,
#         ']' : 0,
#         '<' : 0,
#         '>' : 0
#     }
#     reverseDict = {
#         ')' : '(',
#         '}' : '{',
#         ']' : '[',
#         '>' : '<'
#     }
#     for i in inputString:
#         if inputDict.get(i) == None: continue
#         elif i == '(' or i == '{' or i == '[' or i == '<':
#             inputDict[i] += 1
#         else:
#             rev = reverseDict[i]
#             if inputDict[i] + 1 > inputDict[rev]:
#                 return -1
#             else:
#                 inputDict[i] += 1
#     answer = inputDict['('] + inputDict['{'] + inputDict['['] + inputDict['<']
#     return answer
#
# # print(solution('>_<'))
# # print(solution('if (Count of eggs is 4.) {Buy milk.}'))
# # print(solution('line [plus]'))
# # print(solution('Hello, world!'))
# # print(solution('([)]'))
# print(solution('([])'))

# 4번
# def solution(snapshots, transactions):
#     transactionDict = {}
#     answerDict = {}
#     for snapshot in snapshots:
#         account, money = snapshot[0], snapshot[1]
#         answerDict[account] = int(money)
#     for t in transactions:
#         if transactionDict.get(t[0]) == None:
#             transactionDict[t[0]] = t[1:]
#
#
#     for transaction in transactionDict.values():
#         print(transaction)
#         cmd, account, money = transaction[0], transaction[1], int(transaction[2])
#         if cmd == 'SAVE':
#             answerDict[account] = answerDict.get(account, 0) + money
#         else:
#             answerDict[account] = answerDict.get(account, 0) - money
#
#     return [[a, str(answerDict.get(a))] for a in sorted(answerDict.keys())]
#
# print(solution([
#   ["ACCOUNT1", "100"],
#   ["ACCOUNT2", "150"]
# ], [
#   ["1", "SAVE", "ACCOUNT2", "100"],
#   ["2", "WITHDRAW", "ACCOUNT1", "50"],
#   ["1", "SAVE", "ACCOUNT2", "100"],
#   ["4", "SAVE", "ACCOUNT3", "500"],
#   ["3", "WITHDRAW", "ACCOUNT2", "30"]
# ]
# ))

# 3번
# def solution(dataSource, tags):
#     answer = []
#     tagDict = {}
#     for data in dataSource:
#         doc, ts = data[0], set(data[1:])
#         # print(ts)
#         compare = len(tags) - len(ts - set(tags))
#         # print(len(compare))
#         print(compare)
#         tagDict[compare] = tagDict.get(compare, []) + [doc]
#     print(tagDict)
#     print(sorted(tagDict.keys(), reverse=True))
#     for d in sorted(tagDict.keys(), reverse=True):
#         for doc in tagDict[d]:
#             if d > 0:
#                 answer.append(doc)
#             if len(answer) == 10: break
#     return answ
#
# print(solution([
#     ["doc1", "t1", "t2", "t3"],
#     ["doc2", "t0", "t2", "t3"],
#     ["doc3", "t1", "t6", "t7"],
#     ["doc4", "t1", "t2", "t4"],
#     ["doc5", "t6", "t100", "t8"]
# ], ["t1", "t2", "t3"]
# ))


# 3번
def solution(road, n):
    answer = 0
    maxVal = 0
    fixCnt = 0
    back = 0
    forward = 0
    for idx, r in enumerate(road):
        if r == 1:
            back += 1
        else:
            if fixCnt < 0:
                fixCnt += 1
                i = idx+1
                while road[i] == 0:
                    forward += 1
                maxVal = back + forward + 1
            else:
                maxVal =
    return answer