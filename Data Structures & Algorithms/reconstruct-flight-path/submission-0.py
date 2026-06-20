class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n=len(tickets)
        adjL=collections.defaultdict(list)

        # visited=set()
        # visited.add("JFK")

        tickets.sort()
        # minHeap=[[0,"JFK"]]
        for src,dst in tickets:
            adjL[src].append(dst)

        res=["JFK"] #DF! dont write res=[]
        def dfs(node):
            if len(res)==1+len(tickets):
                return True

            if node not in adjL:#we cant go anywhere from node=> dead end. must do backtracking
                return False
            # cost,node=heapq.heappop(minHeap) #finding which edge from a given node has the least weight

            for i,nei in enumerate(list(adjL[node])):
                res.append(nei)
                adjL[node].pop(i) #pop the place at the ith place

                if dfs(nei)==True:
                    return True#if we found a valid path

                res.pop()#do backtracking only if a valid path hasnt been found
                adjL[node].insert(i,nei)#line 29,30=backtracking
            return False#imp

        dfs("JFK")
        return res