class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt=0
        visited=set()

        edgeMap={i:[] for i in range(n)}
        for u,v in edges:
            edgeMap[u].append(v)
            edgeMap[v].append(u)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in edgeMap[node]:
                dfs(nei)

            visited.add(node)
            return

        for node in range(n):
            if node not in visited:
                cnt+=1
                dfs(node)

        return cnt