function robHouse(houses) {
    let rob1 = 0;
    let rob2 = 0;

    for (money of houses) {
        let tmp = Math.max(money + rob1, rob2);
        rob1 = rob2;
        rob2 = tmp;
    }
    return rob2;
}


console.log(robHouse([1, 2, 3, 1]))