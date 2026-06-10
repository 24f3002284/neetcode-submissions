class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # q=deque()
        preMap={i:[] for i in range(numCourses)}
        visited=set()

        for crs,prs in prerequisites:
            preMap[crs].append(prs)

        def dfs(crs):
            if crs in visited: #a loop
                return False
            if preMap[crs]==[]: # no prerequisite=> the crs can be chosen=>true
                return True

            for pre in preMap[crs]:
                visited.add(crs) #can be outside the for loop
                # dfs(pre) wrong
                if not dfs(pre):#imp!! lines 19,20
                    return False

            visited.remove(crs)
            preMap[crs]=[] #we have already found out that all its prerequisites can be completed(using the for loop)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
