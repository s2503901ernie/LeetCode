class Solution:
    def findLatestTime(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] != '?' or s[i] == ':':
                continue
            if i == 0:
                if s[1] != '?' and int(s[1]) <= 1:
                    s = '1' + s[1:]
                elif s[1] == '?':
                    s = '1' + s[1:]
                else:
                    s = '0' + s[1:]
            if i == 1:
                if s[0] == '0':
                    s = s[0] + '9' + s[2:]
                else:
                    s = s[0] + '1' + s[2:]
            if i == 3:
                s = s[:3] + '5' + s[4]
            if i == 4:
                s = s[:4] + '9'
        return s

