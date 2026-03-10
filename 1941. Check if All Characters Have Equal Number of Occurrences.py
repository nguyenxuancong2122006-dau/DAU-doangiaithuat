class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        
        count = Counter(s)
        values = list(count.values())
        
        return len(set(values)) == 1