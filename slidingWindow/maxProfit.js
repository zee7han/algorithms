function maxProfit(arr){
    let left = 0
    let right = 1
    let maxProfit = 0

    while(right < arr.length){
        if(arr[left] < arr[right]){
            let profit = arr[right] - arr[left]
            maxProfit = Math.max(maxProfit, profit)
        } else {
            left = right
        }
        right++
    }
    return maxProfit
}


console.log(maxProfit([7,1,5,3,6,4]))