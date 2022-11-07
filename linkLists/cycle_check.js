function cycleCheck(Node) {
    let p1 = Node
    let p2 = Node

    while(p2 && p2.next && p2.next.next){
        p1 = p1.next
        p2 = p2.next.next
        if(p1==p2){
            return true
        }
    }

    return false
}