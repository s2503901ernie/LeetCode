class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d1 = set()
        d2 = set()
        ans = 0
        for c in word:
            if c.islower():
                d1.add(c)
            else:
                d2.add(c)
        for c in d1:
            if c.upper() in d2:
                ans += 1
        return ans