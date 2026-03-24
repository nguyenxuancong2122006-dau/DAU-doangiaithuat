class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        
        # tách
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        # sort
        even.sort()              # tăng dần
        odd.sort(reverse=True)   # giảm dần
        
        # gán lại
        e = o = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even[e]
                e += 1
            else:
                nums[i] = odd[o]
                o += 1
        
        return nums