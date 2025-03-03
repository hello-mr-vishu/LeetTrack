class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {}
        for i in range(numCourses):
          premap[i]=[]
        # print(premap)
        for crs , pre in prerequisites:
          premap[crs].append(pre)
        # print(premap)
        visitSet = set()
        def dfs(crs):
          # print(visitSet,"1")
          if crs in visitSet:
            # print("executed1")
            return False
          if premap[crs] == []:
            # print(crs,"executed2")
            return True
          # print("executed3")
          visitSet.add(crs)
          # print(visitSet,"2")
          for pre in premap[crs]:
            if not dfs(pre): return False
          visitSet.remove(crs)
          premap[crs] = []
          # print(premap)
          return True
        for crs in range(numCourses):
          # print("***************",crs , "executed0")
          if not dfs(crs): 
            # print("executed4")
            return False
        return True