function combinationSum(arr, target){
    let output = []
    dfs(0,[],0,arr, output, target)
    return output
}

function dfs(i, curr, total, arr, output, target) {
    if(total == target){
        output.push(JSON.stringify(curr))
        return
    }
    if(i >= arr.length || total > target){
        return
    }

    curr.push(arr[i])
    dfs(i, curr, (total + arr[i]), arr, output, target)

    curr.pop()
    dfs(i+1, curr, total, arr, output, target)
}

console.log(combinationSum([1,2,3,4,6,10,12],12))