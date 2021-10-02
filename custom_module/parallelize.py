from unittest.mock import Mock
import heapq


def time_gone(x):
    return x.t - 1


'''
class Node:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def __lt__(self, other):
        if self.A < other.A:   #오름차순
            return True
        elif self.A == other.A:
            return self.B > other.B  #첫번재 변수가 같으면 두번재 변수로 내림차순
        else:
            return False

    def __str__(self):
        return 'A : {}, B : {}'.format(self.A, self.B)
'''



'''
은행에 100개의 키오스크가 있다.
손님이 차례로 들어오고 앞번호부터 키오스크에 차례대로 입장한다.
손님마다 걸리는 시간이 다르고, 앞 손님의 업무부터 차례로 완료된다.

키오스크가 모두 차있을 경우 손님은 앞 키오스크부터 줄을 서기 시작한다.
대기가 가장 적은 키오스크부터, 대기가 가장 적은 키오스크가 여러개라면 가장 앞번호인 키오스크에 대기한다.

키오스크 


'''


class Node:
    def __init__(self, arg1: int, arg2: str, arr: list):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arr = arr

    def __lt__(self, other):
        if self.arg1 < other.arg1:
            return True
        elif self.arg1 == other.arg1:
            return len(self.arr) > len(other.arr)
        return False

        # elif self.arg1 == other.arg1:
        #     print('hello')
        #     return len(self.arr) > len(other.arr)
        #
        # else:
        #     return False

    def __str__(self):
        return f'arg1: {self.arg1} // arg2: {self.arg2}'

a = Node(1, 'a', [1, 2, 3])
b = Node(8, 'b', [1, 2, 3])
c = Node(5, 'c', [1, 2, 3])
d = Node(6, 'd', [1, 2, 3])
e = Node(7, 'e', [1, 2, 3])
f = Node(4, 'f', [1, 2, 3, 4])
g = Node(3, 'g', [1, 2, 3])
h = Node(2, 'h', [1, 2, 3])

'''
a h f g c d e b
'''


# print(a)
hq = []


heapq.heappush(hq, a)
heapq.heappush(hq, b)
heapq.heappush(hq, c)
heapq.heappush(hq, d)
heapq.heappush(hq, e)
heapq.heappush(hq, f)
heapq.heappush(hq, g)
heapq.heappush(hq, h)


# heapq.heapify(hq)

while hq:
    print(heapq.heappop(hq))

# print(hq)
# for arg in hq:
#     print(arg)
# print([arg for arg in hq])
