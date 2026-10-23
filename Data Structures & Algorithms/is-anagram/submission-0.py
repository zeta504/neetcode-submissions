class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        conta = {}
        for i in range(len(s)):
            conta[s[i]] = conta.get(s[i], 0) + 1
            conta[t[i]] = conta.get(t[i], 0) - 1
        
        return all(v == 0 for v in conta.values())
        