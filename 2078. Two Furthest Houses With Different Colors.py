class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        res = 0
        
        # so với phần tử đầu
        for i in range(n):
            if colors[i] != colors[0]:
                res = max(res, i)
        
        # so với phần tử cuối
        for i in range(n):
            if colors[i] != colors[n-1]:
                res = max(res, n - 1 - i)
        
        return res