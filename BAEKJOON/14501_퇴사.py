<<<<<<< HEAD
=======

>>>>>>> c387d7d6312ff7dd543fded428f80d12ebfe4bbc
def resign(day, money):
    global max_money
    if day >= n:
        max_money = max(max_money, money)
        return
<<<<<<< HEAD
=======

>>>>>>> c387d7d6312ff7dd543fded428f80d12ebfe4bbc
    if day + time[day] <= n: # 일이 가능한 날이라면
        resign(day + time[day], money + pay[day])  # 그 날 일을 하는 경우
        resign(day + 1, money) # 그 날 일을 하지 않는 경우
    else: # 일이 불가능하다면
        resign(day+1, money) # skip

n = int(input())
time = []
pay = []
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)
max_money = 0
resign(0, 0)
<<<<<<< HEAD
print(max_money)
=======
print(max_money)

>>>>>>> c387d7d6312ff7dd543fded428f80d12ebfe4bbc
