/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

function two_sum(arr, target) {
    for(let i=0; i<arr.length; i++){
        let complement = target - arr[i]
        if(arr.includes(complement)){
            console.log("inside here.........", arr[i], complement);
            let j = arr.indexOf(complement)
            if(i !== j){
                return [i,j]
            }
        }
    }
}

console.log(two_sum([3,2,4],6))