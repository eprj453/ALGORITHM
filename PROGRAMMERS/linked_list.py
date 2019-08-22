class Node:
    def __init__(self, item):
        self.node = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


def solution(L, x):
    if x < L[0]:
        L.insert(0, x)
        return L
    if x > L[len(L)-1]:
        L.insert(len(L), x)
        return L
    for idx in range(len(L)-1):
        if x > L[idx] and x < L[idx+1]:
            L.insert(idx+1, x)
            break
    return L

print(solution([1,2,3,4,5], 0))