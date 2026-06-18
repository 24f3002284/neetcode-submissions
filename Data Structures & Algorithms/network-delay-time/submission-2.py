class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #building adj list
        adj=collections.defaultdict(list)
        for src,dst,t in times:
            adj[src].append([dst,t])

        minHeap=[(0,k)] #time,node
        visited=set()
        # visited.add(k)
        ans=0

        while minHeap:
            time,node=heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            ans=max(ans,time)
            
            for nei,t in adj[node]:
                if nei not in visited:
                    
                    heapq.heappush(minHeap,[time+t,nei])
                    # ans=max(ans,time+t)

        # for i in range(1,n+1):
        #     if i not in visited:
        #         return -1

        if len(visited)!=n:
            return -1
        
        return ans
            