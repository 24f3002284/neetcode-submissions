class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r=0,0
        ans=[]
        q=collections.deque() # if we use a vector, we will have to find max=>O(n) for each window
        # use a deque to find min or max each time(elements- stored in descending order)

        while r<len(nums):
            while q and nums[q[-1]]<nums[r]: # imp!!while loop not if. shd keep on popping till all numbers in the deq are less than the current element
                q.pop()
            
            q.append(r)

            if l>q[0]: # to check if the sliding window can contain the leftmost number, we have to store indices in the deq
                q.popleft()

            if r>=k-1:
                ans.append(nums[q[0]])
                l+=1

            r+=1

        return ans
