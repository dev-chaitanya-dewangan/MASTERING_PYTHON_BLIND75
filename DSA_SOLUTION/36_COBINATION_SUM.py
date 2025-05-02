class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res=[]
        nums.sort()
        
        def backtracking(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return 
            for j in range(i,len(nums)):
                if total + nums[j] > target :
                    return 
                cur.append(nums[j])
                backtracking(j,cur,total+nums[j])        
                cur.pop()
        backtracking(0,[],0)
        return res

"""
METHOD TO SOLVE 
START WITH FIRST INDEX AND CHECK ALL REPEATING COMBINATION THEN
IF TOTAL IS MORE THAN TARGET STOP AND MOVE TO THE NEXT INDEX 
TILL THE LAST INDEX AND APPEND THE VALID  COMBINATION IN THE RES 
"""
