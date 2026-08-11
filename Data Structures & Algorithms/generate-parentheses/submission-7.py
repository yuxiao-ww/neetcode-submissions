class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(i, open, close):
            if open == close == n:
                res.append("".join(path))
                return
            
            if open < n:
                path.append("(")
                dfs(i + 1, open + 1, close)
                path.pop()
            
            if close < open:
                path.append(")")
                dfs(i + 1, open, close + 1)
                path.pop()
        dfs(0, 0, 0)
        return res