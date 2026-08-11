class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        if sorted(s) == sorted(t):
            return True
        else:
            return False