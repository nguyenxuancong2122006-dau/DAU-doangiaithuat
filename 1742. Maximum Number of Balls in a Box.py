class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        count = {}

        for i in range(lowLimit, highLimit + 1):
            box = sum(int(d) for d in str(i))
            count[box] = count.get(box, 0) + 1

        return max(count.values())