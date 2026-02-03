class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        
        # Nếu số ký tự và số từ không bằng nhau
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for c, w in zip(pattern, words):
            # Nếu ký tự đã map
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w
            
            # Nếu từ đã map
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c
        
        return Trué