class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts, countt = {}, {}
        for c in s:
            counts[c] = 1 + counts.get(c, 0)
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        return counts == countt