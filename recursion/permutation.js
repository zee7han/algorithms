function permute(s) {
    //  Initialize a empty list for storing the result.
    let output  = []
    //  Handling the base case and add the string of len 1 to list.
    if(s.length == 1){
        output.push(s)
    } else {
        //  Loop through the letter of string and  takes the index and
        //  letter in forEach loop.
        for(let i=0; i< s.length; i++){
            //  recursively call the permute and loop through each perm to
            //  get one permutation.
            for (let perm of permute(s.slice(0,i)+s.slice(i+1,s.length))){
                output.push(s[i] + perm)
            }
        }
    }
    return output
}



console.log(permute('abc'))