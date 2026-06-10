class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]

        def backtracking(idx,subset):
            if idx==len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[idx])
            backtracking(idx+1,subset)

            while idx<len(nums)-1 and nums[idx]==nums[idx+1]:
                idx+=1

            subset.pop()
            backtracking(idx+1,subset)

        backtracking(0,[])
        return ans