# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        start = head
        while start:
            end = start  
            sum = 0
            while end.val != 0:
                sum += end.val
                end = end.next
            start.val = sum  
            start.next = end.next  
            start = start.next 
        return head

"""
        modify = head.next  # Start from the node after the initial 0
        next_sum = modify

        while next_sum:
            total = 0
            # Find the sum of all nodes until you encounter a 0.
            while next_sum.val != 0:
                total += next_sum.val
                next_sum = next_sum.next

            # Assign the sum to the current node's value.
            modify.val = total
            # Move next_sum to the first non-zero value of the next block.
            next_sum = next_sum.next
            # Move modify also to this node.
            modify.next = next_sum
            modify = modify.next

        return head.next  # Skip the initial 0 node
"""