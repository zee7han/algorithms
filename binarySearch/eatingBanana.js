function eatingBananaPiles(piles, h){
    let l = 1
    let r = Math.max( ...piles )

    let res = r

    while(l<r){
        let k = Math.floor((l+r)/2)
        let hours = 0
        for(let i=0;i<piles.length;i++){
            hours += Math.ceil(piles[i]/k)
        }
        if(hours <= h){
            Math.min(res,k)
            r=k-1
        } else {
            l=k+1
        }
    }
    return res
}