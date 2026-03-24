class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        
        total = 0
        for num in nums:
            if count[num] == 1:
                total += num
                
        return total