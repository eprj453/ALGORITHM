def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)

    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a, k , input, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    ans = []
    # print('(', end = ' ')
    for i in range(k+1):
        if a[i]:
            ans.append(i)
            # print(i, end = ' ')
    # print(')', end = ' ')
    sum = 0
    for num in ans:
        sum += num
    if sum == 10:
        print(ans, end=' ')

MAXCANDIDATES = 100
NMAX = 100
a = [0]*NMAX
backtrack(a, 0, 10)
