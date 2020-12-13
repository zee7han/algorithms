function maxWater(arr) {
    let len = arr.length
    let maxWater = 0

    for(let i=0; i< len; i++){
        let lft = arr[i]
        for(let j=0; j<i; j++){
            lft = Math.max(arr[j],lft)
        }

        let rgt = arr[i]
        for(let j=i+1; j<len; j++){
            rgt = Math.max(arr[j],rgt)
        }
         maxWater = maxWater + (Math.min(lft,rgt)-arr[i])
    }
    return maxWater
}

console.log(maxWater([0, 1, 0, 2, 1, 0,1, 3, 2, 1, 2, 1]));
