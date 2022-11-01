function maxProduct(arr, n) {
    let result = arr[0]

    for(let i=0; i<n; i++){
        let mul = arr[i]
        for(let j= i+1; j<n; j++) {
            result = Math.max(mul, result)
            mul *= arr[j]
        }
        result = Math.max(mul, result)
    }
    return result
}

let arr = [ 1, -2, -3, 0, 7, -8, -2 ];
console.log(maxProduct(arr,arr.length));