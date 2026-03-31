class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bước 1: loại phần tử trùng liên tiếp
        arr = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                arr.append(nums[i])
        
        # Bước 2: đếm hill và valley
        count = 0
        
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                count += 1
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                count += 1
        
        return count