class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        arr = []
        
        for i in range(0, len(nums), 2):
            arr.append(nums[i+1])
            arr.append(nums[i])
        
        return arr