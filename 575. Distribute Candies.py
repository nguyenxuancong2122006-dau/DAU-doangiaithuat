class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique_types = len(set(candyType))
        return min(unique_types, len(candyType) // 2)