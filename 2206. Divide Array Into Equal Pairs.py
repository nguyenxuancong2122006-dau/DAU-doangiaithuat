class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        
        for val in count.values():
            if val % 2 != 0:
                return False
                
        return True