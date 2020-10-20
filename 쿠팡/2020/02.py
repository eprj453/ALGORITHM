from datetime import datetime as dt, timedelta
import heapq as hq
from queue import PriorityQueue as pq

class Bank:
    def __init__(self):
        self.using_kiosk = []
        self.unusing_kiosk = []

    def find_kiosk(self):
        if self.unusing_kiosk: # 쓰이지 않는 키오스크가 있다면
            sorted_kiosk = sorted(self.unusing_kiosk, key=lambda x: (x.last_used, x.number))
        else:
            sorted_kiosk = sorted(self.using_kiosk, key=lambda x: (x.customer.end, x.number))
        return sorted_kiosk.pop(0)

    def check_kiosk(self, time):
        


class Kiosk:
    def __init__(self, number):
        self.customer = None
        self.waiting = []
        self.number = number
        self.used = False
        self.last_used = None

    def add_customer(self, new_customer):
        if not self.customer:
            self.customer = new_customer
        else:
            self.waiting.append(new_customer)


class Customer:
    def __init__(self, start, end):
        self.start = start
        self.end = end




def make_datetime(date, time):
    month, day = list(map(int, date.split('/')))
    hour, minute, sec = list(map(int, time.split(':')))
    return dt(month=month, day=day, hour=hour, minute=minute, second=sec)

def solution(n, customers):
    answer = 0
    bank = Bank()
    for k in range(n):
        bank.unusing_kiosk.append(Kiosk(k))
    for customer in customers:
        date, time, take_time = customer.split()
        arrival = make_datetime(date, time)
        end_time = arrival + timedelta(minutes=take_time)
        new_customer = Customer(arrival, end_time)
        kiosk = bank.find_kiosk()
        kiosk.add_customer(new_customer)
        bank.using_kiosk.append(kiosk)

        for k in bank.using_kiosk: # 시간 감소시키키
            if k.customer and k.customer.end <= arrival:
                if k.waiting:
                    k.customer = k.waiting.pop(0)
                else:
                    bank.using_kiosk.remove(k)
                    bank









# def solution(n, customers):
#     answer = 0
#     bank = Bank()
#     for i in range(n):
#         hq.heappush(bank.kiosk, [])
    # using_kiosk = []
    # unusing_kiosk = []
    # using_check = [False] * n
    # hq.heapify(using_kiosk)
    # kiosks = {i:0 for i in range(n)}
    # current_time = 0
    # for customer in customers:
    #     date, time, take_time = customer.split()
    #     arrival = make_datetime(date, time)
    #     current_time = arrival
    #     end_time = arrival + timedelta(minutes=take_time)
    #     if len(using_kiosk) < n:
    #         idx = using_check.index(False)
    #         using_kiosk[idx] = True
    #         kiosks[idx] += 1
    #         waiting = []
    #         hq.heappush(using_kiosk, [end_time, idx, waiting])
    #     else:
    #         pass
    #
    # if current_time:
    #     while using_kiosk:
    #         kiosk = using_kiosk
    #
