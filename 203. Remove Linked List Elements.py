class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        
        curr = dummy
        
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next  # xóa node
            else:
                curr = curr.next           # đi tiếp
        
        return dummy.next