class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r=0,0
        n=len(nums)-1
        moves=0
        

        while r<n:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            
            l=r+1
            r=farthest
            
            moves+=1

        return moves