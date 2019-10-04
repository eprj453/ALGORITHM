import sys, time
sys.stdin = open('1952_input.txt', 'r')

def register(s, schedule, fare):
    global min_fare

    # if fare >= min_fare:
    #     return

    if s >= n:
        min_fare = min(fare, min_fare)
        return

    if schedule[s] == 0:
        register(s+1, schedule, fare)

    elif schedule[s] > 0:
        register(s+1, schedule, fare + (d * schedule[s]))
        register(s+1, schedule, fare + m)
        register(s+3, schedule, fare + m_3)
        register(s+12, schedule, fare + y)



for i in range(1, int(input())+1):
    # start = time.time()
    d, m, m_3, y = map(int, input().split())
    sche = list(map(int, input().split()))
    n = len(sche)
    min_fare = 3000 * 12
    register(0, sche, 0)
    print('#{} {}'.format(i, min_fare))


    # print("time :", time.time() - start)