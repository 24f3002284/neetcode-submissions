class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        rank=[1 for i in range(len(edges)+1)] #rank=no. of nodes connected to the component with it as root
 
        def findParent(node):
            if parent[node]!=node:
                parent[node]=findParent(parent[node])

            return parent[node]

        def union(node1,node2):
            # if parent[node1]==parent[node2]:
            #     return False
            p1,p2=findParent(node1),findParent(node2)
            if p1==p2:
                return False

            if rank[p1]>rank[p2]:
                rank[p1]+=rank[p2]
                parent[p1]=p2
            else:
                rank[p2]+=rank[p1]
                parent[p2]=p1

            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        # return True