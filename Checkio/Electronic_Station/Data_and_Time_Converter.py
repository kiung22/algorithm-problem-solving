def date_time(time):
    time = time.replace('.', ' ').replace(':', ' ').split()
    date, month, year, hour, minute = time

    m = {'01': 'January', '02': 'February', '03': 'March',
                  '04': 'April', '05': 'May', '06': 'June',
                  '07': 'July', '08': 'August', '09': 'September',
                  '10': 'October', '11': 'November', '12':'December'}

    h = 'hours'
    min = 'minutes'
    if int(hour) == 1:
        h = 'hour'
    if int(minute) == 1:
        min = 'minute'

    return f"{int(date):01d} {m[month]} {year} year {int(hour):01d} {h} {int(minute):01d} {min}"
