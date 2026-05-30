class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in dic:
                dic[ss] = [s]
            else:
                dic[ss].append(s)
        return list(dic.values())