# A gene string can be represented by an 8-character long string, with choices 
# from 'A', 'C', 'G', and 'T'. 
# 
#  Suppose we need to investigate a mutation from a gene string start to a gene 
# string end where one mutation is defined as one single character changed in the 
# gene string. 
# 
#  
#  For example, "AACCGGTT" --> "AACCGGTA" is one mutation. 
#  
# 
#  There is also a gene bank bank that records all the valid gene mutations. A 
# gene must be in bank to make it a valid gene string. 
# 
#  Given the two gene strings start and end and the gene bank bank, return the 
# minimum number of mutations needed to mutate from start to end. If there is no 
# such a mutation, return -1. 
# 
#  Note that the starting point is assumed to be valid, so it might not be 
# included in the bank. 
# 
#  
#  Example 1: 
# 
#  
# Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA",
# "AAACGGTA"]
# Output: 2
#  
# 
#  Example 3: 
# 
#  
# Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC",
# "AACCCCCC"]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  start.length == 8 
#  end.length == 8 
#  0 <= bank.length <= 10 
#  bank[i].length == 8 
#  start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T']. 
# 
#  
# 
#  Related Topics Hash Table String Breadth-First Search 👍 1794 👎 184
from typing import List


class Solution1:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1

        d = {}
        stack = [[start, 0]]
        while stack:
            cur, c = stack.pop(0)
            for b in bank:
                if self.diff(cur, b) > 1:
                    continue
                if d.get(b, float('inf')) > c + 1:
                    d[b] = c + 1
                    stack.append([b, c + 1])
        return d.get(end, -1)

    def diff(self, w1, w2):
        n = 0
        for i in range(8):
            if w1[i] != w2[i]:
                n += 1
        return n


class Solution2:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        w = {
            "A": ["T", "C", "G"],
            "T": ["A", "C", "G"],
            "C": ["A", "T", "G"],
            "G": ["A", "T", "C"],
        }
        d = {}
        if end not in bank:
            return -1
        stack = [[start, 0]]
        while stack:
            cur, c = stack.pop(0)
            for i in range(8):
                for word in w[cur[i]]:
                    new = cur[:i] + word + cur[i+1:]
                    if new not in bank:
                        continue
                    if d.get(new, float('inf')) > c + 1:
                        d[new] = c + 1
                        stack.append([new, c + 1])
        return d.get(end, -1)
