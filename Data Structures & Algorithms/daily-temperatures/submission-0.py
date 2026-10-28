class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        before = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while before and temperatures[before[-1]] < temp:
                j = before.pop()
                res[j] = i - j
            before.append(i)
        return res