def sun_angle(time):
    time = time.split(':')
    hour = int(time[0]) + int(time[1])/60
    angle = (hour-6) * 15
    if not angle  > 180:
        return angle
    return "I don't see the sun!"
