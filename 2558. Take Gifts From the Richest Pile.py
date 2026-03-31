class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        # tạo max heap bằng cách đảo dấu
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        
        for _ in range(k):
            largest = -heapq.heappop(heap)
            remaining = int(math.sqrt(largest))
            heapq.heappush(heap, -remaining)
        
        return -sum(heap)