"""
 valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


Constraints:

0 <= s.length <= 20
s consists of digits only.
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        ans = []
        for i in range(1, 4):
            first = s[:i]
            if self.isvalid(first) is False:
                continue
            for j in range(i+1, i+4):
                second = s[i:j]
                if self.isvalid(second) is False:
                    continue
                for k in range(j+1, j+4):
                    third = s[j:k]
                    if self.isvalid(third) is False:
                        continue
                    last = s[k:]
                    if self.isvalid(last) is False:
                        continue
                    ans.append(first + '.' + second + '.' + third + '.' + last)

        return ans

    def isvalid(self, string):
        if not string:
            return False
        if int(string) > 255:
            return False
        value = int(string)
        if len(str(value)) != len(string):
            return False
        return True
