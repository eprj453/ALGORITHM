# trie 자료구조
# 문자열 검색에 효과적인 자료구조. Tree 구조이다.
# 검색의 시간 복잡도는 O(n)으로 빠른 편이지만 공간 복잡도가 매우 크기 때문에 메모리를 엄청나게 잡아먹을 수 있다.

class Trie:
    def __init__(self):
        self.head = Node(None) # head는 문자가 없는 Node
        self.stringCount = 0

    def add(self, string):
        n = self.head
        n.stringLength[len(string)] = n.stringLength.get(len(string), 0) + 1
        self.stringCount += 1
        l = len(string)-1
        for ch in string:
            if ch not in n.children: # 글자가 존재하지 않는다면
                n.children[ch] = Node(ch) # 새로운 Node를 추가.
            n.stringLength[l] = n.stringLength.get(l, 0) + 1
            l -= 1
            n.childrenCount += 1
            n = n.children[ch]
        n.terminal = string # 맨 마지막에

    def find(self, string, l):
        n = self.head
        for ch in string:
            if ch not in n.children: # 자식에 포함되어 있지 않은 경우
                # print('return')
                return 0 # 없는 문자열
            n = n.children[ch]
            # print(n.childrenCount)
        return n.stringLength.get(l, 0)

class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.terminal = None
        self.stringLength = {}
        self.childrenCount = 0


def solution(words, queries):
    answer = []
    trie = Trie()
    back_trie = Trie()
    for word in words:
        trie.add(word)
        back_trie.add(''.join(list(reversed(word))))

    for query in queries:
        idx = len(query)
        l = query.count('?')
        # if query[0] == '?' and query[-1] == '?':
        #     res = tree.find(self.head.)
        if query[0] == '?': # 뒤쪽부터 찾기
            string = ''
            idx = len(string)-1
            while query[idx] != '?':
                string += query[idx]
                idx -= 1
            print(string, len(query) - len(string))
            res = back_trie.find(string, len(query) - len(string)-1)
            answer.append(res)
        else: # 앞쪽부터 찾기
            string = ''
            idx = 0
            while query[idx] != '?':
                string += query[idx]
                idx += 1
            print(string, len(query) - len(string))
            res = trie.find(string, len(query) - len(string)-1)
            answer.append(res)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

#


aaa = 'abcde?fg'
print(aaa[0:-2])
print(ord('a')-97)
#
# trie = Trie()
# back_trie = Trie()
#
# trie.add('apple')
# trie.add('appll')
# trie.add('asdss')
# trie.add('bf')
# trie.add('bfddfffs')
# print(trie)
# print(trie.find('bfs'))





# class Trie:
#     def __init__(self):
#         self.head = Node(None) # head는 문자가 없는 Node
#         self.stringCount = 0
#
#     def add(self, string):
#         n = self.head
#         n.stringLength[len(string)] = n.stringLength.get(len(string), 0) + 1
#         self.stringCount += 1
#         l = len(string)-1
#         for ch in string:
#             # print(type(n.children))
#             if not n.children[ord(ch)-97]: # 글자가 존재하지 않는다면
#                 # print(ch)
#                 n.children[ord(ch)-97] = Node(ch) # 새로운 Node를 추가.
#             n.stringLength[l] = n.stringLength.get(l, 0) + 1
#             l -= 1
#             n.childrenCount += 1
#             n = n.children[ord(ch)-97]
#         n.terminal = string # 맨 마지막에
#
#     def find(self, string, l):
#         n = self.head
#         for ch in string:
#             if not n.children[ord(ch)-97]: # 자식에 포함되어 있지 않은 경우
#                 # print('return')
#                 return 0 # 없는 문자열
#             n = n.children[ord(ch)-97]
#             # print(n.childrenCount)
#         return n.stringLength.get(l, 0)
#
# class Node:
#     def __init__(self, ch):
#         # print(char)
#         self.char = ord(ch) - 97 if ch else None
#         temp = []
#         for _ in range(26):
#             temp.append([])
#         self.children = temp
#         self.terminal = None
#         self.stringLength = {}
#         self.childrenCount = 0
#
#
# def solution(words, queries):
#     # print(words)
#     answer = []
#     trie = Trie()
#     back_trie = Trie()
#     for word in words:
#         # print(word)
#         trie.add(word)
#         back_trie.add(''.join(list(reversed(word))))
#
#     for query in queries:
#         idx = len(query)
#         l = query.count('?')
#         # if query[0] == '?' and query[-1] == '?':
#         #     res = tree.find(self.head.)
#         if query[0] == '?': # 뒤쪽부터 찾기
#             string = ''
#             idx = len(string)-1
#             while query[idx] != '?':
#                 string += query[idx]
#                 idx -= 1
#             # print(string, len(query) - len(string))
#             res = back_trie.find(string, len(query) - len(string)-1)
#             answer.append(res)
#         else: # 앞쪽부터 찾기
#             string = ''
#             idx = 0
#             while query[idx] != '?':
#                 string += query[idx]
#                 idx += 1
#             # print(string, len(query) - len(string))
#             res = trie.find(string, len(query) - len(string)-1)
#             answer.append(res)
#     return answer