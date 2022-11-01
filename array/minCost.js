function minCost(cost, m, n) {
    if (m < 0 || n < 0) {
        return Number.MAX_SAFE_INTEGER
    } else if (m == 0 && n == 0) {
        return cost[m][n]
    } else {
        return cost[m][n] + 
        minimum(minCost(cost, m - 1, n - 1), 
        minCost(cost, m - 1, n), 
        minCost(cost, m, n - 1))
    }
}

function minimum(x, y, z) {
    if (x < y) {
        if(x<z){
            return x
        } else{
            return z
        }
    } else {
        if(y<z){
            return y
        } else{
            return z
        }
    }
}

let cost = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]

console.log(minCost(cost, 2, 2))