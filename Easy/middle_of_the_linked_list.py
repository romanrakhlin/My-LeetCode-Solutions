"""
really interesting problem and I guess that created
really efficient algorithm
my idea idea is:
1) find the length of a linked list
2) create a formula to find the middle element
3) iterate through each node till I find a middle
and then return this node
"""

class Solution:
    # 1
    def find_len(self, head):
        cur_node = head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count
        
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2
        middle = (self.find_len(head) // 2) + 1
        
        # 3
        cur_node = head
        count = 0
        while cur_node is not None:
            count += 1
            if count == middle:
                return cur_node
            cur_node = cur_node.next
            
"""
but the most efficiant algorithm is slow and fast pointer method
"""
class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow