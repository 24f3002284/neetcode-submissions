class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree=> all nodes r connected with no cycle
        visited=set()
        cycle=set()
        edgeMap={c:[] for c in range(n)}

        if len(edges)!=n-1: #invalid tree
            return False

        for u,v in edges:
            edgeMap[u].append(v)
            edgeMap[v].append(u)

        def dfs(node,parent):
            if node in cycle and node!=parent:
                return False
            if node in visited:
                return True

            cycle.add(node)
            for nei in edgeMap[node]:
                if nei==parent:
                    continue
                else:
                    if not dfs(nei,node):
                        return False

            cycle.remove(node)
            visited.add(node)
            return True # we have processed all nei of the node and each of them returned true=>none of them make it an invalid tree

        return dfs(0,-1) and len(visited)==n