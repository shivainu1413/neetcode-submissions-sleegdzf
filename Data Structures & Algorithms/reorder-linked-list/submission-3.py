# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        first = head

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev
        
        dummy = ListNode()
        curr = dummy
        while first and second:
            curr.next = first
            first = first.next
            curr = curr.next
            
            curr.next = second
            second = second.next
            curr = curr.next
        if first: 
            curr.next = first