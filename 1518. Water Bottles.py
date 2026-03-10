class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drink = numBottles
        empty = numBottles

        while empty >= numExchange:
            new = empty // numExchange
            drink += new
            empty = new + empty % numExchange

        return drink