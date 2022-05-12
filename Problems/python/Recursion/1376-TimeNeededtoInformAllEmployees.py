"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.



Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
Example 2:


Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.


Constraints:

1 <= n <= 105
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
"""
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ans = []
        self.dfs(0, ans, headID, manager, informTime, n)

        return max(ans)

    def dfs(self, cur, ans, idx, manager, info, n):
        if info[idx] == 0:
            ans.append(cur)
            return
        for i in range(n):
            if manager[i] == idx:
                new = cur + info[idx]
                self.dfs(new, ans, i, manager, info, n)


class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ans = []
        emp = []
        for i in range(n):
            if informTime[i] == 0:
                emp.append(i)

        while emp:
            i = emp.pop()
            cur = 0
            while True:
                if i == -1:
                    break
                i = manager[i]
                cur += informTime[i]

            ans.append(cur)

        return max(ans)


class Solution3:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = {}
        ans = []
        for i in range(n):
            if manager[i] not in d:
                d[manager[i]] = [i]
            else:
                d[manager[i]].append(i)
        self.dfs(0, d, headID, ans, manager, informTime)


        return max(ans)

    def dfs(self, cur, d, idx, ans, manager, info):
        if idx not in d:
            ans.append(cur)
            return
        for emp in d[idx]:
            new = cur + info[idx]
            self.dfs(new, d, emp, ans, manager, info)
