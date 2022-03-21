def solution(tickets):
    adj = {}
    for start, end in tickets:
        if not adj.get(start):
            adj[start] = []
        adj[start].append(end)
    for start in adj:
        adj[start].sort(reverse=True)
    answer = []
    stack = ["ICN"]
    while stack:
        current_airport = stack[-1]

        if adj.get(current_airport):
            stack.append(adj[current_airport].pop())
        else:
            answer.append(stack.pop())

    return answer[::-1]
