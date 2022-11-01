function threeSum(arr){
    let result = []
    arr = arr.sort((a,b)=>{return a-b})
    for(let i=0; i<arr.length;i++){
        if(i>0 && arr[i]==arr[i-1]){
            continue
        } 
        let left = i+1
        let right = arr.length-1

        while(left < right){
            let threeSum = arr[i] + arr[left] + arr[right]
            if(threeSum > 0){
                right--
            } else if(threeSum < 0){
                left++
            } else {
                result.push([arr[i],arr[left],arr[right]])
                left++
            }
        }
    }
    return result
}

console.log(threeSum([-1,0,1,2,-1,-4]))