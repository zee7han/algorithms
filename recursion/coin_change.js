function dyn_coin_change(target, coins, memory) {
    let min_coins = target

    if (coins.includes(target)) {
        memory[target] = 1
        return 1
    } else if (memory[target] > 0) {
        return memory[target]
    } else {
        for (c = 0; c < coins.length; c++) {
            let num_coins
            if (coins[c] <= target) {
                num_coins = 1 + dyn_coin_change(target - coins[c], coins, memory)
            }
                    if (num_coins < min_coins) {
                        min_coins = num_coins
                        memory[target] = min_coins
                    }
        }
    }
    return min_coins
}

let memory = new Array(80).fill(0)
console.log("result==", dyn_coin_change(63, [1, 5, 10, 25], memory))