class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        for pre in range(numCourses):
          prereq[pre] = []
        # print(preMap)
        for crs,pre in prerequisites:
          prereq[crs].append(pre)
        # print(preMap)
        output = []
        visit ,cycle = set() , set()
        def dfs(crs):
          if crs  in cycle:
            return False
          if crs in visit:
            return True
          cycle.add(crs)
          for pre in prereq[crs]:
            if dfs(pre) == False:
              return False
          cycle.remove(crs)
          visit.add(crs)
          output.append(crs)
          return True
        for c in range(numCourses):
          if dfs(c) == False:
            return []
        return output