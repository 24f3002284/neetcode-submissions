class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap=[[] for crs in range(numCourses)]
        visited=set()

        for pre,crs in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visited: # a loop
                return False
            if preMap[crs]==[]:
                return True # we can complete the course since it has no prereq

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            preMap[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True