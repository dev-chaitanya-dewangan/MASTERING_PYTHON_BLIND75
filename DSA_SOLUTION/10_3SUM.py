def threeSum(nums):
    res=[] # RESULT LIST OF THREE LIST INTEGER ELEMENTS WHICH SUMS TO ZERO
    # SORTING CUASE THIS ARRANGES ELEMENT SUCH WHERE WE CAN EASILY DETECT DUPLICATES
    nums.sort() 
    # ENUMERATE BEACUSE IT GIVES BOTH ELEMENT AND THE INDEX 
    # LOOPING FOR EVERY ELEMENT 
    for i,curr in enumerate(nums):
        print(i)
        #IF CURRENT IS JUST LIKE PREVIOUS NUMBER (i-1) IT SKIPS IT 
        if i>0 and curr==nums[i-1] :
            continue

        # TWO POINTERS LEFT AND RIGHT (LEFT-> ELEMENT FROM CURRENT INDEX ; RIGHT-> LAST INDEX FROM LIST(which is sorted) )
        left,right=i+1 ,len(nums)-1
        
        #LOOP THORUGH UNTIL MEET AT CENTER
        while left < right :
            #THIS(threesum) CALCULATES THREE NUMEBER CURRENT NUMBER + LEFT POINTER AND RIGHT POINTER
            threesum=curr+nums[left]+nums[right]
            # WHEN THREESOM IS BIGGER THAN ZERO THEN SHIRFT POINTER TO INDEX FROM LAST INDEX TO PREVIUOUS INDEX
            if threesum > 0:
                right -=1
            elif threesum < 0 :
                left +=1
            else:
                res.append([curr,nums[left],nums[right]])
                left +=1
                while nums[left]==nums[left-1] and l<r:
                    l +=1
    return res
threeSum([-1,0,1,2,-1,-4])
print(threeSum([-1,0,1,2,-1,-4]))

"""
TIME COMPLEXITY  : O(N^2)
SPACE COMPLEXITY : O(1)
"""

"""
METHOD TO SOLVE :
TWO POINTER APPRAOCH :
WE ONLY HAVE TO CHECK IF CURRENT NUMBER IS NOT AS PREVIOUS THEN FIND WITH TWO POINTER IS THERE TWO NUMBER THAT ADDS UP TO ZERO WITH ADDITION TO CURRENT NUMBER 
THEN APPEND IT TO THE RESULT LIST ,RETURN THE RESULT LIST 
-------------------------------------------------------------------------------------------
PSUEDO CODE
1.SORT THE GIVEN LIST OF NUMBERS
2.LOOP THOUGH EVERY ELEMENT AND SKIP IF DUPLICATE (WHEN WE SEE NUMBER AS PREVIOUS ELEMENT WE SKIP IT )
3.DEFINE TWO POINTER WHICH TRACKS THE LIST (LEFT ONLY CHECK FROM INDEX OF CURRENT LIST)
4.LOOP UNTIL LEFT AND RIGHT CONVERGE AND CHECK IF THREE NUMBER CURRENT NUMBER,LEFT & RIGHT POINTER NUMBER (curr+nums[left]+nums[right]) ADDS UPTO ZERO 
5.THEN INCREMENT AND DECREMENT RESPESTIVE TO LEFT AND RIGHT (AND ALSO INCREMENT MORE WHEN WE SEE DUPLICATE AS SEEN IN PREVIOUS LEFT NUMBER )
-------------------------------------------------------------------------------------------


"""