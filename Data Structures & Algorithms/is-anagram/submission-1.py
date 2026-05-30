class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        tt = sorted(t)
        return ss == tt


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        td = defaultdict(int)
        for ss in s:
            sd[ss] += 1
        for tt in t:
            td[tt] += 1
        return sd == td