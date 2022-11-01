function maxWater(arr){
    let maxWater = 0

    for(let i=0; i<arr.length; i++){
        let left = arr[i]

        for(let j=0; j<i;j++){
            left = Math.max(arr[j],left)
        }
        let right = arr[i]
        for(let j=i+1; j<arr.length;j++){
            right = Math.max(arr[j],right)
        }

        maxWater = maxWater + (Math.min(left,right)-arr[i])
    }
    return maxWater
}


console.log(maxWater([0, 1, 0, 2, 1, 0,1, 3, 2, 1, 2, 1]));
