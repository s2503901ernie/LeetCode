class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        b = {}
        for c in circles:
            r = c[2]
            for i in range(c[0]-r+1, c[0]+r):
                for j in range(c[1]-r+1, c[1]+r):
                    if i not in b:
                        b[i] = {j}
                    else:
                        b[i].update({j})
            b[c[0]].update({c[1]+c[2]})
            b[c[0]].update({c[1]-c[2]})
            if c[0] + c[2] not in b:

                b[c[0]+c[2]] = {c[1]}
            else:
                b[c[0]+c[2]].update({c[1]})
            if c[0]-c[2] not in b:
                b[c[0]-c[2]] = {c[1]}
            else:
                b[c[0]-c[2]].update({c[1]})
        ans = 0
        for key in b.keys():
            ans += len(b[key])

        return ans
