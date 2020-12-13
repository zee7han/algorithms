/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/

function ListNode(val,next) {
    this.val = val
    this.next = next
}

let a = new ListNode(2,null)
let b = new ListNode(4,null)
let c = new ListNode(3,null)

a.next = b
b.next = c

let d = new ListNode(5,null)
let e = new ListNode(6,null)
let f = new ListNode(4,null)

d.next = e
e.next = f

function addTwoNumbers(l1, l2) {
    let output = null
    const carry = arguments[2]
    
    if(l1 || l2){
        const val1 = l1 ? l1.val : 0
        const val2 = l2 ? l2.val : 0
        const nex1 = l1 ? l1.next : null
        const nex2 = l2 ? l2.next : null

        let output_val = carry?(val1 + val2 + 1):(val1 + val2)
        output  = new ListNode(output_val%10)
        output.next = addTwoNumbers(nex1,nex2,output_val>9)
    } else if(carry){
        output = new ListNode(1)
        output.next = null
    }
    return output
};

console.log(addTwoNumbers(a,d));
