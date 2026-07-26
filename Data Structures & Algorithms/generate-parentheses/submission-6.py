class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(path, open, close):
            if open == close == n:
                res.append("".join(path))
                return
            
            if open < n:
                path.append("(")
                dfs(path, open + 1, close)
                path.pop()
            
            if close < open:
                path.append(")")
                dfs(path, open, close + 1)
                path.pop()
        
        dfs(path, 0, 0)
        return res