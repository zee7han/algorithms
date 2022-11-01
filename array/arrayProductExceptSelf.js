function arrayProductExceptSelf(arr){
    let output = new Array(arr.length).fill(1)
    
    let prefix = 1
    for(let i=0; i<arr.length; i++){
        output[i] = prefix
        prefix = prefix * arr[i]
    }

    let postfix = 1
    for(let i=output.length-1; i>=0; i--){
        output[i] = output[i]*postfix
        postfix = postfix*arr[i]
    }
    return output
}

console.log(arrayProductExceptSelf([1,2,3,4]))