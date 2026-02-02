class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1. Đếm tần suất
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        # 2. Bucket sort theo tần suất
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        
        # 3. Lấy k phần tử có tần suất cao nhất
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res