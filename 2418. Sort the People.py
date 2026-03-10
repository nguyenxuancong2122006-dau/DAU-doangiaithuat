class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = list(zip(names, heights))
        people.sort(key=lambda x: x[1], reverse=True)
        return [name for name, h in people]