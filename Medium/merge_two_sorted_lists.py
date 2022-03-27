class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        result = ListNode()
        helper = result
        while l1 and l2:
            if l1 is None or l2 is None:
                if l1:
                    helper.next = l1
                else:
                    helper.next = l2
            else:
                if l1.val < l2.val: # >
                    helper.val = l1.val
                    helper.next = ListNode(l2.val)
                else: # <=
                    helper.val = l2.val
                    helper.next = ListNode(l1.val)
            if l1.next or l2.next:
                helper.next.next = ListNode()
            helper = helper.next.next
            l1 = l1.next
            l2 = l2.next
        return result