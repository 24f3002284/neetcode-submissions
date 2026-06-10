class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        def backtracking(idx,subset:list):
            if idx==len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[idx])
            backtracking(idx+1,subset)
            subset.pop()
            backtracking(idx+1,subset)

        backtracking(0,[])
        return ans