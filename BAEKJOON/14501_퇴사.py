<<<<<<< HEAD

=======
>>>>>>> 428ea1dcc7b03202b8c937bcf431bfdc2bf3ab03
def resign(day, money):
    global max_money
    if day >= n:
        max_money = max(max_money, money)
        return
<<<<<<< HEAD
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
print(max_money)

=======
    if day + time[day] <= n: # 상담 가능한 경우
        resign(day + time[day], money + pay[day]) # 상담한다
        resign(day+1, money) # 안하고 skip
    else:
        resign(day+1, money) # 상담 불가능한 경우
>>>>>>> 428ea1dcc7b03202b8c937bcf431bfdc2bf3ab03

n = int(input())
time = []
pay = []
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)
max_money = 0
resign(0, 0)
print(max_money)