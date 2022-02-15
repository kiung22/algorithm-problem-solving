def hour_to_minute(time):
    hour, minute = time.split(":")
    return int(hour)*60 + int(minute)


def get_fee(time, fees):
    fee = fees[1]
    if time <= fees[0]:
        return fee
    fee += ((time-fees[0]) // fees[2] + bool((time-fees[0]) % fees[2])) * fees[3]
    return fee


def solution(fees, records):
    cars_dict = {}
    for record in records:
        time, car_number, state = record.split()
        if state == "IN":
            cars_dict[car_number] = cars_dict.get(car_number, 0) - hour_to_minute(time)
        else:
            cars_dict[car_number] += hour_to_minute(time)
    for car_number in cars_dict:
        if cars_dict[car_number] <= 0:
            cars_dict[car_number] += hour_to_minute("23:59")

    answer = []
    for car_number in sorted(cars_dict.keys()):
        answer.append(get_fee(cars_dict[car_number], fees))

    return answer
