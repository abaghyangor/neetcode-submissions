class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq = dict()
        t_freq = dict()

        for i in range(len(s)):
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1
        
        for letter in t_freq:
            if t_freq[letter] != s_freq.get(letter, 0):
                return False
        return True

        