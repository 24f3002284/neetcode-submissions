class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        perms=[]
        visited=[False for _ in nums]

        def backtracking(perms):
            if len(perms)==len(nums):
                ans.append(perms.copy())
                return

            for i in range(len(nums)):
                if visited[i]==False:
                    perms.append(nums[i])
                    visited[i]=True
                    
                    backtracking(perms)

                    #backtracking
                    perms.pop()
                    visited[i]=False
                    
            
            # if visited[idx]==False:
            #     perms.append(nums[idx])
            #     visited[idx]=True
            #     backtracking(idx+1,perms)
                
            #     #backtracked
            #     perms.pop()
            #     visited[idx]=False
            #     backtracking(idx+1,perms)

        backtracking(perms)
        return ans
            
            