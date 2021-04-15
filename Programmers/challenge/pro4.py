def solution(n, z, roads, queries):
    w_dict = {}
    for road in roads:
        w_dict[road[2]] = (road[0], road[1])
    
    location = [0]
    dp = [0]
    ans = []

    for c in queries:
        while c >= len(dp):
            n = len(dp)
            if n % z == 0:
                dp.append(n//z)
                location.append(0)
            else:
                max_value = 10000000000
                min_value = max_value
                min_location = 0
                for w in w_dict.keys():
                    if 0 <= n-w and dp[n-w] != -1:
                        value = dp[n-w] + 1 + (w_dict[w][0] != location[n-w])
                        if value < min_value:
                            min_value = value
                            min_location = w_dict[w][1]
                if min_value == max_value:
                    dp.append(-1)
                    location.append(0)
                else:
                    dp.append(min_value)
                    location.append(min_location)

        ans.append(dp[c])

    return ans

print(solution(5, 5, [[1,2,3],[0,3,2]], [0,1,2,3,4,5,6]))