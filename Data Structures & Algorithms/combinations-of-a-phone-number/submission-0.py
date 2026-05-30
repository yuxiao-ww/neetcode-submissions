class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        
        def backtracking(path, index):
            if index == len(digits):
                result.append(path[:])
                return
            
            for letter in mapping[digits[index]]:
                backtracking(path+letter, index + 1)
        
        backtracking('', 0)
        return result



 