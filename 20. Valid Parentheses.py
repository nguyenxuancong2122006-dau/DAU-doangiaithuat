class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for c in s:
            # nếu là dấu mở
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                # nếu stack rỗng → sai
                if not stack:
                    return False
                
                top = stack.pop()
                
                # kiểm tra khớp
                if c == ')' and top != '(':
                    return False
                if c == ']' and top != '[':
                    return False
                if c == '}' and top != '{':
                    return False
        
        # cuối cùng stack phải rỗng
        return len(stack) == 0