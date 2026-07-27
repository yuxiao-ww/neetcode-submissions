class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 每个node的parent都是自己
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            # 一路往上找真正的parent
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # 共同parent
            if p1 == p2:
                return 0
            
            # rank为了防止tree越来越高
            if rank[p1] > rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res