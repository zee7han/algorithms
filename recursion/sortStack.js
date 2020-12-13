function sortStack(stack) {
    if(stack.length !== 0){
        let temp = stack.pop()
        sortStack(stack)
        sortedInsert(stack, temp);
    }
}

function sortedInsert(stack,el) {
    if(stack.length === 0 || el > stack[stack.length-1]){
        stack.push(el)
    } else {
        let temp = stack.pop()
        sortedInsert(stack,el)
        stack.push(temp)
    }
}
