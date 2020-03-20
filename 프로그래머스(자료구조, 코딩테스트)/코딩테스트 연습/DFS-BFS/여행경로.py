def solution(tickets):
    answer = []
    airport_dict = {}
    ticket_check = {}
    for ticket in tickets:
        flight, arrived = ticket[0], ticket[1]
        airport_dict[flight] = airport_dict.get(flight, []) + [arrived]
        airport_dict[flight].sort()
        ticket_check[(flight, arrived)] = ticket_check.get((flight, arrived), 1)
    print(airport_dict)
    stk = ['ICN']
    while stk:
        # print('stk :', stk)
        # print(ticket_check)
        flight = stk[-1]
        arrive_airports = airport_dict.get(flight)
        if arrive_airports and ticket_check.get((flight, arrive_airports[0])) == 1:
            arrived = arrive_airports[0]
            stk.append(arrived)
            # answer.append(arrived)
            ticket_check[(flight, arrive_airports[0])] = 0
            arrive_airports.pop(0)
        else:
            answer.append(stk.pop())




    # print(ticket_visited)
    # print(ticket_check)
    # answer.reverse()
    return list(reversed(answer))

# [["ICN", "AAA"], ["AAA", "ICN"], ["ICN", "BBB"],["BBB", "ICN"],["CCC", "AAA"],["AAA", "CCC"], ["CCC", "DDD"], ["DDD", "CCC"], ["BBB", "DDD"]]
print(solution([["ICN", "AAA"], ["AAA", "ICN"], ["ICN", "BBB"],["BBB", "ICN"],["CCC", "AAA"],["AAA", "CCC"], ["CCC", "DDD"], ["DDD", "CCC"], ["BBB", "DDD"]]))