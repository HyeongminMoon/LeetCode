# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        up = 0
        head = None
        past = None
        while(l1 or l2):
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s = (a + b + up) % 10
            up = (a + b + up) // 10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            node = ListNode(s)
            if head is None:
                head = node
            if past:
                past.next = node
            past = node
        
        if up:
            node = ListNode(up)
            past.next = node
        
        return head
        
        