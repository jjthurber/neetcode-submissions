class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = set(s)
        set2 = set(t)
        if (len(s) == len(t)):
            return sorted(s) == sorted(t)
        else:
            return False