class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()

        def backtracking(idx,combination:list,target):
            if target==0:
                ans.append(combination.copy())
                return
            if idx>=len(candidates) or target<0:
                return

            combination.append(candidates[idx])
            backtracking(idx+1,combination,target-candidates[idx])
            combination.pop()
            while idx<len(candidates)-1 and candidates[idx]==candidates[idx+1]:
                idx+=1 
            backtracking(idx+1,combination,target)

        backtracking(0,[],target)
        return ans