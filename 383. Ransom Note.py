class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = defaultdict(int)
        
        for ch in magazine:
            count[ch] += 1
        
        for ch in ransomNote:
            if count[ch] == 0:
                return False
            count[ch] -= 1
        
        return True