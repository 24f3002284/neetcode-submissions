class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        combination=[]

        def backtracking(idx,combination,tar):
            if tar<0 or idx>=len(nums):
                return
            if tar==0:
                res.append(combination.copy())
                return 

            # for i in range(idx,len(nums)):
            combination.append(nums[idx])
            backtracking(idx,combination,tar-nums[idx])
            combination.pop()
            backtracking(idx+1,combination,tar)

        backtracking(0,combination,target)
        return res