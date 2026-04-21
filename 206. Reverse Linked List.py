class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next      # lưu node tiếp theo
            curr.next = prev     # đảo chiều
            
            prev = curr          # tiến prev
            curr = nxt           # tiến curr
        
        return prev