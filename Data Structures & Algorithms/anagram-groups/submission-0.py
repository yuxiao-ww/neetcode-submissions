class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        result = []
        for item in strs:
            sorted_item = ''.join(sorted(item))
            dic[sorted_item].append(item)
        
        for _, value in dic.items():
            result.append(value)
        
        return result