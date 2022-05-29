class BookMyShow:

    def __init__(self, n: int, m: int):
        self.s = [[0 for _ in range(m)] for _ in range(n)]
        self.m = n
        self.n = m

    def gather(self, k: int, maxRow: int) -> List[int]:
        d = {}
        j = -1
        for i in range(maxRow + 1):
            d = {}
            n = 0
            for r in range(self.n):
                if self.s[i][r] == 0:
                    j = r
                    break
            if j == -1:
                continue
            while j < self.n and n < k:
                if self.s[i][j] == 0:
                    d[n] = [i, j]
                    n += 1
                    j += 1
                else:
                    break
        if len(d) == k:
            n = 0
            print(d)
            for k in d.keys():
                i, j = d[k][0], d[k][1]
                if n == 0:
                    ans = [i, j]
                    n += 1
                self.s[i][j] = 1
            return ans
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        d = {}
        n = 0
        for i in range(maxRow + 1):
            for j in range(self.n):
                if n == k:
                    break
                if self.s[i][j] == 0:
                    d[n] = [i, j]
                    n += 1
        if len(d) == k:
            print(d)
            for k in d.keys():
                i, j = d[k][0], d[k][1]
                self.s[i][j] = 1
            return True
        return False



# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)