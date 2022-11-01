function pairSum(arr, target) {
    let seen = {}
    let output = []

    for(let i=0; i<arr.length; i++){
        let k = target - arr[i]
        if(!seen.hasOwnProperty(k)){
            seen[arr[i]] = i
        } else{
            output.push([Math.min(k,arr[i]),Math.max(k,arr[i])])
        }
    }
    return output
}

console.log(pairSum([1,3,2,2],4))
