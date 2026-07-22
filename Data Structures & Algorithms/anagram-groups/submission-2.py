class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            map[ss].append(s)
        return list(map.values())