class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def backtracking(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return 
            if total > target or i==len(candidates):
                return 
            cur.append(candidates[i])
            backtracking(i+1,cur,total+candidates[i])
            cur.pop()
            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            backtracking(i+1,cur,total)
        backtracking(0,[],0)
        return res

"""
METHOD TO SOLVE THIS 
SORT THE GIVEN LIST 
THEN START WITH FIRST INDEX AND MAKE MAKE COMBINATION WITHOUT REPEATING THE 
NUMBER AGAIN THEN RECURSIVELY MAKE COMBINATION UNTIL 
WE HAVE VALID COMBINATION AND APPEND IT TO RESULT AND INCREMENT THE INDEX 
"""