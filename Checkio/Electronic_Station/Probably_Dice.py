def probability(dice_number, sides, target):
    from itertools import product
    dice = [range(1, sides +1) for x in range(0,dice_number)]
    count = 0
    result = []

    for x in product(*dice):
        if sum(x) == target:
            result.append(sum(x))

    return len(result)/sides ** dice_number

print(probability(2,6,3))
