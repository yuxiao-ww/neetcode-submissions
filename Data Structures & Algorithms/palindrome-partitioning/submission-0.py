class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]
        
        def backtracking(path, start):
            if start == len(s):
                result.append(path[:])
                return
            
            for end in range(start+1, len(s)+1):
                sub = s[start:end]
                if isPalindrome(sub):
                    path.append(sub)
                    backtracking(path, end)
                    path.pop()
        
        result = []
        backtracking([], 0)

        return result
        