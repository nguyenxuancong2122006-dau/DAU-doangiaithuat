class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))   # sắp xếp ký tự
            groups[key].append(s)
        
        return list(groups.values())