class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = n * (n + 1) // 2
        x = int(S ** 0.5)
        
        if x * x == S:
            return x
        return -1