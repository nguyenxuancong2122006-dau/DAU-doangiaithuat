class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # bỏ ký tự không phải chữ/số
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # so sánh (không phân biệt hoa thường)
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True