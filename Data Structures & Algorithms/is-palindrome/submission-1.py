class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(c.lower() for c in s if c.lower() in "abcdefghijklmnopqrstuvwxyz0123456789" )
        return string == string[::-1]