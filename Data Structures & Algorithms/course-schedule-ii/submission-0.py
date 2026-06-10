class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq={c:[] for c in range(numCourses)}
        for crs,pre in prerequisites:
            preReq[crs].append(pre)

        visited=set() # stores all the nodes that can be completed so that we dont have to chck them again
        cycle=set()
        ans=[]

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited: # has already been marked as "can be completed"
                return True

            cycle.add(crs)
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
                
            cycle.remove(crs)
            visited.add(crs) # crs can be completed
            ans.append(crs) #crs can be complted=> add it to output
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return [] # there is atleast 1 cycle=> no ordering will lead to completion of all courses
        return ans