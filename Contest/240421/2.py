class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = set()
        d1 = set()
        d2 = set()
        used = set()
        for c in word:
            if c.islower():
                d1.add(c)
                if c.upper() in d2:
                    if c in ans:
                        ans.remove(c)
                    used.add(c)
            else:
                d2.add(c)
                if c.lower() in d1 and c.lower() not in used:
                    ans.add(c.lower())
        return len(ans)