# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks_over_bridge = []
    trucks_on_bridge = []
    trucks = truck_weights
    while truck_weights:
        time += 1
        if trucks_on_bridge and trucks_on_bridge[0][0] == time:
            trucks_over_bridge.append(trucks_on_bridge.pop(0))
        if sum([x for t, x in trucks_on_bridge]) + trucks[0] <= weight:
            trucks_on_bridge.append([time + bridge_length, trucks.pop(0)])
    return time + bridge_length


"""
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length

    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return time
"""
