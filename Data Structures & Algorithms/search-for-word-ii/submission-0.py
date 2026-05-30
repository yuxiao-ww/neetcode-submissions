class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # 如果这个节点是单词结尾，存单词


class Solution:
    def findWords(self, board, words):
        # 1. 构建 Trie
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w   # 标记单词结尾

        rows, cols = len(board), len(board[0])
        res = []

        # 2. DFS 搜索
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            nxt = node.children[ch]

            if nxt.word:  # 找到单词
                res.append(nxt.word)
                nxt.word = None  # 避免重复加入

            # 标记访问过
            board[r][c] = "#"
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = ch  # 回溯复原

        # 3. 从每个格子开始 DFS
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res
