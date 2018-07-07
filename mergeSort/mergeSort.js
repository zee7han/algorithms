function mergeSort(arr) {
  if(arr.length == 1) {
    return arr;
  }

  let middle = Math.floor(arr.length/2);
  let left = arr.slice(0, middle);
  let right = arr.slice(middle);

  return merge(
    mergeSort(left),
    mergeSort(right)
  )
}

function merge(left, right){
  let leftIndex = 0;
  let rightIndex = 0;
  let result = [];

  while(leftIndex < left.length && rightIndex < right.length) {
    if(left[leftIndex] < right[rightIndex]){
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }

  //Here we are merging the array
  return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
}





let sample = [1,6,4,7,5,34];
console.log(mergeSort(sample));
