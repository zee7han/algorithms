# Here using the classical recursion which is not feasible for large numbers.
def rec_coin(target,coins):
    # Initially set the mminimum coins to target.
    min_coins = target
    # Handling the base case If coin of target available then return the 1.
    if target in coins:
        return 1
    else:
        # Here loop through every coin in list which is less than the target and
        # recusively call the function for target-i.
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target-i,coins)
            # If num_coins less than min_coins then set min_coins to num_coins.
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


print(rec_coin(25,[1,5,10]))

# Here using the dynamic approach for change coin which gives fast solution for
# large numbers because using the cache.
def dyn_coin(target, coins, known_results):
    min_coins = target
    # Handling the base case If target coin already available then set that target result to 1 and
    # return 1.
    if target in coins:
        known_results[target] = 1
        return 1
    # check for the lookup table or cache if target result greater than 0 then
    # return the value  from lookup table or cache.
    elif known_results[target] > 0:
        return known_results[target]
    else:
        # Here loop through every coin in list which is less than the target and
        # recusively call the function for target-i.
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + dyn_coin(target-i,coins,known_results)
            # If num_coins less than min_coins then set its result in cache or
            #lookup table min_coins to num_coins.
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[target] = min_coins
    return min_coins

# To execute this we initialize the cache of size larger than target.
known_results = [0]*80
print(dyn_coin(63,[1,5,10,25],known_results))
