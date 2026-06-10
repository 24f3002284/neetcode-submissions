class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1

        bucket=[[] for i in range(len(nums)+1)] 
        for n in freq:
            bucket[freq[n]].append(n)

        ans=[]
        i=len(nums)-1
        while k>0:
            
            if bucket[i]!=[]:
                ans.extend(bucket[i])
                k-=len(bucket[i])
            i-=1
            
        return ans