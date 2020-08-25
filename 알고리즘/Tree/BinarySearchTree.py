class BSTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        return self.root.inorder() if self.root else []

    def min(self):
        return self.root.min() if self.root else None

    def max(self):
        return self.root.max() if self.root else None

    # lookup의 입력 인자 : key
    # lookup의 반환 값 : 찾은 Node와 그 부모 Node(부모는 삭제 연산을 하기 위해 필요함)
    def lookup(self, key):
        return self.root.lookup(key) if self.root else None, None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def remove(self, key, data):
        node, parent = self.lookup(key)
        if node:
            return True
        else: # 없애야 하는 Node가 존재하지 않으면 삭제할 Node도 없음.
            return False

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self

    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, parent=self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, parent=self)
            else:
                return None, None
        else:
            return self, parent

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            if key == self.key:
                raise KeyError


    # 삭제 연산
    # 삭제되는 원소가 leaf node인 경우 -> 그냥 삭제
    # 자식을 하나 가지고 있는 경우 -> 자기 자리에 자식을 올림
    # 자식을 둘 가지고 있는 경우 ->