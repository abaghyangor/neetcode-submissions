class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = dict()
        t_freq = dict()

        if len(s) != len(t):
            return False

        for letter in s:
            s_freq[letter] = s_freq.get(letter, 0) + 1
        for letter in t:
            t_freq[letter] = t_freq.get(letter, 0) + 1
        
        for letter in t_freq:
            if letter in s_freq:
                if s_freq[letter] == t_freq[letter]:
                    pass
                else:
                    return False
            else:
                return False
        return True

        