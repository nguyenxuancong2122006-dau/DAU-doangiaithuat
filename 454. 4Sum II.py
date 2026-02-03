class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count = {}
        
        # Tính tất cả tổng của nums1 + nums2
        for a in nums1:
            for b in nums2:
                s = a + b
                count[s] = count.get(s, 0) + 1
        
        res = 0
        
        # Tìm -(c + d)
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in count:
                    res += count[target]
        
        return res