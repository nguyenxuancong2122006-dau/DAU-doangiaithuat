class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)  # đổi sang list để dễ sửa
        
        for i in range(1, len(s), 2):  # duyệt index lẻ
            s[i] = chr(ord(s[i-1]) + int(s[i]))
        
        return "".join(s)