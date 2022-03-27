"""
reallyyyyyy nice and efficiend solution
the solution is a combination of what we already know
1) Floyd's algorithm
2) how to find middle node with it
3) reverse of a linked list
4) understand the traversal of a linked list

so whats the algorithms
this is how the algorithm works (yeahh another list):
1) use the Floyd's algorithm so sinf the middle node
and as you already know that it will be slow 
2) when we found the middle node we have to create
prev and after pointers then reverse linked list
FROM THE MIDDLE NODE and as you know from knowledje
of reversing linked lists the the new head
of reversed linked lists will be prev
3) lets create two "linked lists"
that is normal (head) and reversed (prev)
after that we have to start traversing
through reversed nodes and each iteration
check if they are equal to normal's
if they are not then return False is they are equal
then move reversed forward and normal forvard
and at the end if we look all nodes of both linked lists
and they are equal so while loops ends and we return True
P.S. its no matter that giver lined list elements even or odd
cause u can draw yourself that and that variant and check
to move pointers from begining and meddle node (2nd middle if even nodes)
and compare if its really polindrom then all be okey!!!
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        prev = None
        after = None
        while slow:
            after = slow.next
            slow.next = prev
            prev = slow
            slow = after
            
        # compare first and second half
        reverse = prev
        noramal = head
        while reverse:
            if reverse.val != noramal.val:
                return False
            reverse = reverse.next
            noramal = noramal.next
            
        return True