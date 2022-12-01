# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        linked_list = ListNode(0)
        head = linked_list
        
        while(any([ln for ln in lists])):
            candidate = [ln.val if ln else None for ln in lists]
            min_idxs, min_value = self.myArgmin(candidate)

            for min_idx in min_idxs:
                linked_list.next = ListNode(min_value)
                linked_list = linked_list.next
                lists[min_idx] = lists[min_idx].next
        
        return head.next
            
            
    def myArgmin(self, candidate: List[Union[int, None]]) -> Tuple[List[int], int]:
        min_idxs = []
        min_value = 10**4 + 1
        for i, v in enumerate(candidate):
            if v is not None:
                if v == min_value:
                    min_idxs.append(i)
                elif v < min_value:
                    min_value = v
                    min_idxs = [i]
                
        
        return min_idxs, min_value