class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        
        for x in nums:
            if abs(x) < abs(res):
                res = x
            elif abs(x) == abs(res) and x > res:
                res = x
                
        return res