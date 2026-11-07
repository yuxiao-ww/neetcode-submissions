class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = dict(), dict()
        for c in s:
            ds[c] = 1 + ds.get(c, 0)
        for c in t:
            dt[c] = 1 + dt.get(c, 0)
        return ds == dt