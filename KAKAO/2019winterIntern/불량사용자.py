temp = []
ans = set()
def perm(start, banned_id, user_id, visited):
    global ans
    if start == len(banned_id):
        print(temp)
        res = True
        for i in range(len(banned_id)):
            u, b = temp[i], banned_id[i]
            if len(temp[i]) != len(banned_id[i]):
                return
            for j in range(len(u)):
                # if b[j] == '*': continue
                if u[j] != b[j] and b[j] != '*':
                    res = False
                    break
        if res:
            t = sorted(temp)
            # print(tuple(t))
            ans.add(tuple(t))
            # ans += 1
        return

    for i in range(len(user_id)):
        if visited[i]: continue
        else:
            temp.append(user_id[i])
            visited[i] = True
            perm(start+1, banned_id, user_id, visited)
            temp.pop()
            visited[i] = False



def solution(user_id, banned_id):
    print(banned_id)
    # print()
    # find(0, 0, user_id, banned_id, len(banned_id), banned_id)
    # print(banned_id)
    print([False] * len(user_id))
    perm(0, banned_id, user_id, [False] * len(user_id))
    # subset(user_id, banned_id)
    print(ans)
    answer = len(ans)
    return answer


# print(sorted(["fr*d*", "*rodo", "******", "******"], reverse=True))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# s = set([1,2,3 ])
# q = set([3,2,1])
# print(s == q)
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))