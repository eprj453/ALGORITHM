from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    truck_weights = deque(truck_weights)
    # truck_weights.popleft()
    n = 0
    present_bridge = 0 # 현재 다리 위에 있는 트럭의 총 무게
    while truck_weights or bridge:
        answer += 1
        print('present_bridge :  {}'.format(present_bridge))
        # answer += 1
        while truck_weights and present_bridge + truck_weights[0] <= weight:
            wei = truck_weights[0]
            bridge.append([wei, answer])
            present_bridge += wei
            truck_weights.popleft()
            break
        print('bridge: {}'.format(bridge))
        print('trucks : {}'.format(truck_weights))
        print('answer : {}'.format(answer))
        print()
        while bridge:
            wei, time = bridge[0][0], bridge[0][1]
            # answer : 경과시간, bridge : 다리에 올라탄 시간
            if answer - time == bridge_length-1:
                bridge.popleft()
                present_bridge -= wei
            break
    return answer+1

print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100,[10,10,10,10,10,10,10,10,10,10]))
# print(solution(100, 100, [10]))