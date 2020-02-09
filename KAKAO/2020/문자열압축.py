def solution(s):
    s_len = len(s)
    answer = s_len
    end = (s_len // 2) + 1
    for i in range(1, end):
        string = ""
        # print('초기 string : {}'.format(string))
        num = 1
        first = s[0:i]
        for j in range(i, s_len+i, i):
            # print('compare : {}부터 {}까지'.format(j ,j+i))
            compare = s[j:j+i]
            # print('first : {}'.format(first))
            # print('compare : {}'.format(compare))
            # print('string : {}'.format(string))
            # print()
            if len(first) != len(compare):
                if first == compare:
                    num += 1
                if num > 1:
                    string += str(num)
                string += first
                if compare != "":
                    string += compare
                break

            if first == compare:
                num += 1
            else:
                if num > 1:
                    string += (str(num) + first)
                    # print('{} 추가'.format(str(num)+first))
                else:
                    string += first
                    # print('{} 추가'.format(first))
                first = compare
                num = 1
            first = s[j:j+i]

        #
        #
        #
        # print("string : {}".format(string))
        # print()
        answer = min(len(string), answer)
    return answer
