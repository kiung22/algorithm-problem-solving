def useless_flight(schedule):
    flights = []
    for x in schedule:
        flight = x
        flights.append(flight)
        for y in schedule:
            if flight[1] == y[0]:
                flight[1] = y[0]
                flight[2] += y[2]
                flights.append(flight)
