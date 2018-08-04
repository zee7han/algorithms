def rec_coin(target,coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target-i,coins)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


print(rec_coin(25,[1,5,10]))


def dyn_coin(target, coins, known_results):
    min_coins = target
    if target in coins:
        known_results[target] = 1
        return 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + dyn_coin(target-i,coins,known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[target] = min_coins
    return min_coins

known_results = [0]*80
print(dyn_coin(63,[1,5,10,25],known_results))
