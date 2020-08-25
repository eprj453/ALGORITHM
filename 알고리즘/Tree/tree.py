class BinaryTree:
    def __init__(self):
        self.root = Node(None)

    def insert(self, data):
        if not self.root.data:
            self.root = Node(data)
        else:
            self.root.insert(self.root, data)
        return

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def size(self):
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        # print(left_size, right_size)
        return left_size + right_size + 1

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def insert(self, parent, data):
        if parent.left:
           if parent.right:
               self.insert(self.left, data)
           else:
               parent.right = Node(data)
               return
        else:
            parent.left = Node(data)
            return

    def inorder(self):
        traversal = []

        if self.left:
            traversal += self.left.inorder()

        traversal.append(self.data)

        if self.right:
            traversal += self.right.inorder()

        return traversal

tree = BinaryTree()
tree.insert(1)
print(tree.inorder())
tree.insert(2)
print(tree.inorder())
tree.insert(3)
print(tree.inorder())
tree.insert(4)
print(tree.inorder())
tree.insert(5)
tree.insert(6)
# tree.insert(7)
print(tree.size())
print(tree.inorder())
