# https://leetcode.com/problems/linked-list-cycle

"""
use Floyd's algorithm to solve this problem
as you know this algorithms consists on two parts
first is the met of fast and slow pointers
and other part is to find the start of a cycle
and we actually dont need second part
cause if we find out that slow and fast poiunter met
its a sign that linkedl list has a cycle and
we need to return True overwise return False
also really crucial part is the while loop
we have to check only fast poiunter
cause its moving faster and check
if we can move it forward and that check if
we can move it forward forward only in that order
"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        
        return False