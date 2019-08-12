# 재귀 함수 : 자기 자신을 호출하는 함수
# 재귀 호출 : 재귀적 정의(점화식)을 구현하기 위해 사용

# 그래프의 길이 우선 탐색, 백트래킹 시 자주 사용한다.

# 기본 개념은 반복, for나 while을 사용하지 않고 반복을 사용할 수 있다.

# for i in range(3):
#     print('hello?') >> 보통의 반복문

# 재귀함수의 조건. 몇번 반복할것인가?
# >> 매개변수를 counting하는 조건으로 주어 반복횟수를 조절한다.

# count = 0
# def hello(count):
#     if count < 3:
#         print('hello')
#         hello(count + 1)
# hello(0)


# def hello(count, n):
#     if count == n:
#         print('------------')
#         return
#     else:
#         hello(count + 1, n)
#         print(count, '> hello')
#         # hello(count + 1, n)
#
# hello(2, 8)


# 집에 가서 해볼것.
cnt = 0 # 전역변수가 하나 있다.
def hello(count, n):
    global cnt
    if count == n:
        cnt += 1
        print('------------')
        return
    else:
        hello(count + 1, n)
        hello(count + 1, n)
        print(count, '> hello')
        # hello(count + 1, n)

hello(0, 4)
print(cnt)