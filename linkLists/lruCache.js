class Node {
    constructor(key, value){
        this.key = key
        this.value = value
        this.next = null
        this.prev = null
    }
}

class LRUCache {
    constructor(capacity){
        this.capacity = capacity
        this.cache = {}
        this.left = new Node(0,0)
        this.right = new Node(0,0)
        this.left.next = this.right
        this.right.prev = this.left
    }

    get(key){
        if(this.cache[key]){
            this.remove(this.cache[key])
            this.insertAtRight(this.cache[key])
            return this.cache[key].value
        } else {
            return -1
        }
    }

    put(key, value){
        if(this.cache[key]){
            this.remove(this.cache[key])
        }
        let newNode = new Node(key, value)
        this.insertAtRight(newNode)
        this.cache[key] = newNode

        // As left.next is always the LRU node.
        if(Object.keys(this.cache).length > this.capacity){
            this.remove(this.left.next)
        }
    }

    remove(node){
        let prevNode = node.prev
        let nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    }

    // This is to keep track of most recent used.
    insertAtRight(node) {
        let prevNode = this.right.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = this.right
        this.right.prev = node
    }
}