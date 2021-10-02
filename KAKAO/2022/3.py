import math


def convert_time_to_int(t):
    hour, minute = t.split(':')
    return (int(hour) * 60) + int(minute)


def get_parking_time(in_time, out_time):
    return convert_time_to_int(out_time) - convert_time_to_int(in_time)


def get_parking_fee(fees, parking_time):
    default_time, default_fee, per_time, per_fee = fees

    if parking_time <= default_time:
        return default_fee

    return default_fee + math.ceil(((parking_time - default_time) / per_time)) * per_fee


def solution(fees, records):
    answer = []

    default_time, default_fare, per_time, per_fare = fees

    parking_time_dict = dict()  # key: 차량번호(string) / value: 누적시간(int)
    parking_lot_dict = dict()  # key: 차량번호(string) / value: 입/출 시간(string)
    parking_fee_dict = dict()  # key: 차량번호(string) / value: 요금(int)

    for record in records:
        print(record)
        car_time, car_number, in_out = record.split(' ')
        if in_out == 'IN':  # 입차
            parking_lot_dict[car_number] = car_time
        else:  # 출차
            in_time = parking_lot_dict.pop(car_number)
            parking_time = get_parking_time(in_time, car_time)
            parking_time_dict[car_number] = parking_time_dict.get(car_number, 0) + parking_time

    for car_number, in_time in parking_lot_dict.items():  # 주차장에 남아있는 차는 23:59 출차로 일괄계산
        parking_time = get_parking_time(in_time, '23:59')
        parking_time_dict[car_number] = parking_time_dict.get(car_number, 0) + parking_time

    for car_number, in_time in parking_time_dict.items():  # 모든 차량 주차시간 계산
        parking_fee_dict[car_number] = parking_fee_dict.get(car_number, 0) + get_parking_fee(fees, parking_time_dict[
            car_number])
        # print()

    parking_fee_list = sorted(parking_fee_dict.items(), key=lambda x: x[0])  # 차 번호순으로 정렬
    answer = [fee for car_number, fee in parking_fee_list]

    return answer


a = solution([180, 5000, 10, 600],
             ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
              "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
print(a)
