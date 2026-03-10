class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import collections
        
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        words = paragraph.lower().split()
        banned = set(banned)
        
        count = collections.Counter()
        
        for w in words:
            if w not in banned:
                count[w] += 1
        
        return max(count, key=count.get)