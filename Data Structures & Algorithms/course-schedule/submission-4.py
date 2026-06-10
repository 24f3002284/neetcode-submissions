class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap=[[] for crs in range(numCourses)]
        cycle=set() #to detect cycle
        visit=set()

        for pre,crs in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle: # a loop
                return False
            if crs in visit:
                return True # we can complete the course since it has no prereq

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            # preMap[crs]=[]
            visit.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True