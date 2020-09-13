class Tree:
    def __init__(self):
        self.head = Node(None)
        self.cnt = 0

    def add(self, info):
        n = self.head
        for i in range(len(info)-1):
            inf = info[i]
            if inf not in n.children:
                n.children[inf] = Node(inf)
            n = n.children[inf]

        score = int(info[-1])
        if not n.scores:
            n.scores = [score]
        else:
            n.scores.append(score)
        # print(n.scores)

    def get_score_sum(self, node, query, i):

        n = self.head if i == 0 else node
        if not n: return 0

        if i >= 4:
            for s in n.scores:
                if s >= int(query[i]):
                    # print(n.scores)
                    self.cnt += 1
            return

        if query[i] == '-':
            for key in n.children.keys():
                self.get_score_sum(n.children.get(key), query, i + 1)
        else:
            self.get_score_sum(n.children.get(query[i]), query, i + 1)


class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.scores = None


def solution(info, query):
    answer = []
    tree = Tree()
    for i in info:
        tree.add(i.split())
    # print(tree.head.children)
    for q in query:
        qu = q.split()
        and_count = qu.count('and')
        while and_count:
            qu.remove('and')
            and_count -= 1
        # print(qu)
        tree.get_score_sum(None, qu, 0)
        answer.append(tree.cnt)
        # print('get_cnt : ',tree.cnt)
        tree.cnt = 0
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
