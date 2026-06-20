class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjL=[]
        n=len(points)
        adjL={i:[] for i in range(n)}

        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                cost=abs(x1-x2)+abs(y1-y2)
                adjL[i].append([cost,j])
                adjL[j].append([cost,i]) #imp!!!DG

        #st. pnt let it be 0
        visited=set()
        res=0

        minHeap=[[0,0]]
        
        while minHeap:#bcz, we need the min val each time we pop
            if len(visited)==n:
                return res

            cost,pnt=heapq.heappop(minHeap)
            if pnt in visited:
                continue
            visited.add(pnt)
            res+=cost

            for neiCost,nei in adjL[pnt]:
                heapq.heappush(minHeap,[neiCost,nei])

        return res

