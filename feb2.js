//merge two sorted lists
var mergeTwoLists = function(l1, l2) {
    if (!l1) return l2;
    else if (!l2) return l1;
    else if (l1.val <= l2.val) {
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;
    } else {
        l2.next = mergeTwoLists(l1, l2.next);
        return l2
    }
};

var mergeTwoLists = function(l1, l2) {
    if (!l1) return l2;
    else if (!l2) return l1;
    else if (l1.val <= l2.val) {
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;
    } else {
        l2.next = mergeTwoLists(l1, l2.next);
        return l2
    }
};

// if there is only one list -> return that single list
// else make the current node of the list = to the 'next node' of the first list, recursively passing


// Non-Recursive MergeTwoLists
var mergeTwoLists = function(l1, l2) {
    // if(!l1) return l2
    // if(!l2) return l1
    let curr = new ListNode()
    const dummy = curr
    while(l1 && l2){
        if (l1.val<l2.val){
            curr.next = l1
            l1 = l1.next
    }
        else {
            curr.next = l2
            l2 = l2.next
    }
    curr = curr.next
}
if(l1){
    curr.next = l1
}
if(l2){
    curr.next = l2
}
return dummy.next
};

// Two Numbers
// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.
var addTwoNumbers = function (l1, l2) {
    let dummyHead = new ListNode(0); // Dummy head to simplify the code
    let current = dummyHead;
    let carry = 0;

    while (l1 || l2) {
        let x = l1 ? l1.val : 0;
        let y = l2 ? l2.val : 0;
        let sum = carry + x + y;

        carry = Math.floor(sum / 10);
        current.next = new ListNode(sum % 10);
        current = current.next;

        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }

    if (carry > 0) {
        current.next = new ListNode(carry);
    }

    return dummyHead.next;
};

//reaching points
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        # conditions when false
        if sx > tx or sy > ty:
            return False

        # if we get to the final step
        if sx == tx:
            return (ty- sy) % sx == 0

        if sy == ty:
            return (tx - sx) % sy == 0

        # recursive step
        if tx > ty:
            return self.reachingPoints(sx, sy, tx%ty, ty)

        elif tx < ty:
            return self.reachingPoints(sx, sy, tx, ty%tx)
