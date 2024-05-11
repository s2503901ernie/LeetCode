from collections import deque
from collections import defaultdict


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        up = False
        low = False
        dig = False
        vol = False
        no_vol = False
        d = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for c in word:
            if c.isdigit():
                dig = True
            if c.isupper():
                up = True
            if c.islower():
                low = True
            if c in d:
                vol = True
            if c.isalpha() and c not in d:
                no_vol = True
            if not c.isalpha() and not c.isdigit():
                return False
        return (up or low or dig) and vol and no_vol

