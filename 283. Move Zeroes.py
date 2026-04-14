class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0  # vị trí để đặt số khác 0
        
        # Bước 1: đưa số khác 0 lên trước
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        
        # Bước 2: fill số 0 vào cuối
        for i in range(pos, len(nums)):
            nums[i] = 0