import sys

class Alphabet:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}


class Trie:
    def __init__(self):
        self.start = Alphabet(None)

    def add_word(self, word):
        s = self.start
        for ch in word:
            if ch not in s.children:
                s.children[ch] = Alphabet(ch)
            s = s.children[ch]

        s.children['#'] = None # 단어의 종료

    def get_press_count(self, word):
        s = self.start

        cnt = 0
        for i, ch in enumerate(word):
            # print(f'i : {i}')
            if i == 0: # 첫번째 글자는 무조건 사용자가 입력
                cnt += 1
            else:
                # if s.children and '':
                #     if len(s.children) > 1:
                #         cnt += 1
                if s.children and (len(s.children) > 1):
                    cnt += 1
            s = s.children[ch]

        return cnt


# userInput = input()
while True:
    s = input()
    try:
        if s.isdecimal():
            trie = Trie()
            words = []
            n = int(s)
            for _ in range(n):
                word = input()
                words.append(word)
                trie.add_word(word)

            total_press_count = 0
            for word in words:
                press_cnt = trie.get_press_count(word)
                total_press_count += press_cnt

            answer = total_press_count / n
            print('{:.2f}'.format(answer))
    except EOFError:
        break

# trie = Trie()
#
# words = []
# for _ in range(n):
#     word = input()
#     words.append(word)
#     trie.add_word(word)
#
#
# total_press_count = 0
# for word in words:
#     press_cnt = trie.get_press_count(word)
#     total_press_count += press_cnt
#
# answer = total_press_count / n
# print('{:.2f}'.format(answer))


'''
4
hello
hell
heaven
goodbye
'''