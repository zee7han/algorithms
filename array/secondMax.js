const second_max = (arr) => {
    let max = null 
    let scnd_max = null
    if(arr.length < 2) {
        return -1
    } else {
        arr.forEach(num => {
            if(!isNaN(num)){
                num = Number(num)
                if(max !== null && max > num ) {
                    scnd_max = scnd_max !== null ? Math.max(scnd_max,num) : num
                }
                max = Math.max(max,num)
            }
        });
        return scnd_max = scnd_max == null ? -1 : scnd_max.toString()
    }
}

const second_max2 = (arr) => {
    let max = null
    let scnd_max = null
    if(arr.length < 2){
        return -1
    } else {
        arr.forEach((el)=>{
            let num = Number(el)
            if(max !== null && max > num){
                scnd_max = scnd_max !== null ? Math.max(num,scnd_max) : num
            }
            max = Math.max(max,num)
        })
    }
    return scnd_max = scnd_max == null ? -1 : scnd_max
}

let arr2 = ["3","-2"]
console.log(second_max(arr2));
console.log(second_max2(arr2));

let arr3 = ["5","5","4","2"]
console.log(second_max(arr3));
console.log(second_max2(arr3));

let arr4 = ["4","4","4"]
console.log(second_max(arr4));
console.log(second_max2(arr4));

let arr5 = []
console.log(second_max(arr5));
console.log(second_max2(arr5));

let arr6 = ["-214748364801","-214748364802"]
console.log(second_max(arr6));
console.log(second_max2(arr6));