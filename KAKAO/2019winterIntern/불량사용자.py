ans = 0

def find(u, b, user_id, banned_id, cnt):
    global ans
    if b == len(banned_id):
        if cnt == 0:
            ans += 1
        return

    for i in range(b, len(user_id)):
        b_id = banned_id[i]
        for j in range(u, len(user_id)):
            pass

def solution(user_id, banned_id):
    answer = 0
    return answer


# print(sorted(["fr*d*", "*rodo", "******", "******"], reverse=True))
print(sorted(["frodo", "fradi", "crodo", "abc123", "frodoc"]))