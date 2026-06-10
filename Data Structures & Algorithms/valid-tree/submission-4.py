class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True # EMPTY TREE IS VALID
        
        # valid tree=> all nodes r connected with no cycle
        visited=set()
        cycle=set()
        edgeMap={c:[] for c in range(n)}

        if len(edges)!=n-1: #invalid tree IMP!!! DF THIS EDGE CASE.. check if we have (n-1) edges, sufficient to form a tree
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
                else: #REDUNDANT. NO NEED OF ELSE
                    if not dfs(nei,node):
                        return False

            cycle.remove(node)
            visited.add(node)
            return True # we have processed all nei of the node and each of them returned true=>none of them make it an invalid tree

        return dfs(0,-1) and len(visited)==n #connected=> no. of nodes visited=no. of vertices(nodes)