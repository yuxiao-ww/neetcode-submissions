class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in mapping:
                mapping[ss] = []
            mapping[ss].append(s)
        return list(mapping.values())