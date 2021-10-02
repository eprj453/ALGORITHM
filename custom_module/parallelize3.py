import bisect



def minus_arg(node):
    node.arg1 -= 2
    return node

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


    def __str__(self):
        return f'arg1: {self.arg1} // arg2: {self.arg2} // arr: {self.arr}'

l = []

a = Node(1, 'a', [1, 2, 3])
b = Node(8, 'b', [1, 2, 3])
c = Node(5, 'c', [1, 2, 3])
d = Node(6, 'd', [1, 2, 3])
e = Node(7, 'e', [1, 2, 3])
f = Node(4, 'f', [1, 2, 3, 4])
g = Node(3, 'g', [1, 2, 3])
h = Node(2, 'h', [1, 2, 3])

bisect.insort(l, a)
bisect.insort(l, b)
bisect.insort(l, c)
bisect.insort(l, d)
bisect.insort(l, e)
bisect.insort(l, f)
bisect.insort(l, g)
bisect.insort(l, h)


for i in l:
    print(i)

l[5] = minus_arg(l[5])

print('=============')

for i in l:
    print(i)