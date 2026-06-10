class MedianFinder:

    def __init__(self):
        self.small,self.large=[],[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1*num) # small heap is maxheap

        if self.small and self.large and -1*self.small[0]>self.large[0]:
            heapq.heappush(self.large,-1*heapq.heappop(self.small))

        if len(self.small)>len(self.large)+1:
            heapq.heappush(self.large,-1*heapq.heappop(self.small))

        if len(self.large)>len(self.small)+1:
            heapq.heappush(self.small,-1*heapq.heappop(self.large))

    def findMedian(self) -> float:
        # if (len(small)+len(large))%2==1:
        if len(self.small)>len(self.large): #automatically => that the total length is odd
            return -1*self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]
        
        return (-1*self.small[0]+self.large[0])/2 # even no. of elements
        