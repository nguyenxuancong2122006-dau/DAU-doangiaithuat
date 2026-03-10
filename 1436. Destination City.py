class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start = set()

        for a, b in paths:
            start.add(a)

        for a, b in paths:
            if b not in start:
                return b