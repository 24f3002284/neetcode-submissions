class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap)>1:
            largest=-heapq.heappop(maxHeap)
            secLargest=-heapq.heappop(maxHeap)

            if largest>secLargest: # if largest=secLargest, we need not do anything
                heapq.heappush(maxHeap,-(largest-secLargest))

        return -maxHeap[0] if maxHeap else 0