import sys
sys.stdin = open('5201_input.txt', 'r')

for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse = True)
    truck.sort(reverse= True)
    container_sum = 0
    while truck and container:
        if container[0] <= truck[0]:
            container_sum += container[0]
            container.pop(0)
            truck.pop(0)
        else:
            container.pop(0)
    print('#%d %d'%(i, container_sum))

