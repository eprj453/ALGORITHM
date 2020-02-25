# def solution(participant, completion):
#     d = {} # dictionary
#     for x in participant:
#         d[x] = d.get(x, 0) + 1
#     for x in completion:
#         d[x] -= 1
#
#     dnf = [k for k, v in d.items() if v > 0]
#     answer = dnf[0]
#     return answer
#       내부 hash를 이용해 복잡도 n에 연산 가능

# # 정렬을 이용한다면?
# 정렬 알고리즘의 최적 복잡도는 nlogn,

dict = {
    "1": 1
}
print(dict.get(2, 0))
