import heapq


def minus_arg(node):
    node.arg1 -= 2
    return node


class Node:
    def __init__(self, arg1: int, arg2: str, arr):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arr = arr

    def __lt__(self, other):
        if self.arg1 < other.arg1:
            return True
        elif self.arg1 == other.arg1:
            if len(self.arr) > len(other.arr):
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'arg1: {self.arg1} // arg2: {self.arg2}, arr: {self.arr}'


a = Node(1, 'a', [1, 2, 3])
b = Node(8, 'b', [1, 2, 3])
c = Node(5, 'c', [1, 2, 3])
d = Node(6, 'd', [1, 2, 3])
e = Node(7, 'e', [1, 2, 3])
f = Node(3, 'f', [1, 2, 3, 4])
g = Node(3, 'g', [1, 2, 3, 4, 5])
h = Node(2, 'h', [1, 2, 3])
i = Node(8, 'i', [1, 2, 3,2,2,2,2])
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
heapq.heappush(hq, i)

n = heapq.heappop(hq)
if n.arg1 > 0:
    heapq.heappush(hq, n)

while hq:
    print(heapq.heappop(hq))

heapq.heappush(hq, a)
heapq.heappush(hq, b)
heapq.heappush(hq, c)
heapq.heappush(hq, d)
heapq.heappush(hq, e)
heapq.heappush(hq, f)
heapq.heappush(hq, g)
heapq.heappush(hq, h)
heapq.heappush(hq, i)

for h in hq:
    h = minus_arg(h)

print('==========')

n2 = heapq.heappop(hq)
if n2.arg1 > 0:
    heapq.heappush(hq, n2)




while hq:
    print(heapq.heappop(hq))
