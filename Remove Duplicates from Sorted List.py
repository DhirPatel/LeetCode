# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp1 = temp2 = head
        while temp1:
            if temp1.val == temp2.val:
                temp2.next = temp1.next
            else:
                temp2 = temp2.next
            temp1 = temp1.next
        return head
        