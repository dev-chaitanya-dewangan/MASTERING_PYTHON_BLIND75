
def maxArea(heights):
    # TWO POINTERS
    left,right=0,len(heights)-1
    # RESULT (max heights)
    result=0
    # ITERATE UNTIL IT MEETS AT CENTER 
    while left<right:
        # AREA(area) = LENGTH(right-left ) * HEIGHT(minimum hieght from pointing to elements)
        area=(right-left) * min(heights[right],heights[left])
        # MAXIMUM HIEGHT (comparing both the current area and the stored result changing accordingly which is greater)
        result=max(area,result)
        #WHEN HIEGHT(given in list) IS LESS THAN OR EQUAL TO RIGHT INCREMENT FROM LEFT INDEX 
        if heights[left]<=heights[right]:
            left+=1
        # WHEN RIGHT POINTING HIEGHT(heights[right]) IS LESS THAN LEFT THEN DECREMENT THE POINTER
        else:
             right-=1
#  RETURN THE RESULT
    return result
   

print(maxArea([1,7,2,5,4,7,3,6]))

"""
TIME COMPLEXITY :O(N)
SPACE COMPLEXITY :O(1)


--------------------------------------------------------------------------------------------------------------------

"""

"""
--------------------------------------------------------------------------------------------------------------------

METHOD TO SOLVE THIS 
TWO POINTER APPROACH->
WITH TWO POINTER COMPARING EACH ELEMENTS IN FORMULA (LENGTH*HEIGHT) WHICH IS GREATER UNTIL WWE GET THE MAX AREA.
--------------------------------------------------------------------------------------------------------------------
PSUDE CODE
1.DEFINE TWO POINTER ONE AT LAST AND ONE AT FIRST
2.LOOP THROUGH ELEMENT UNTIL REACHES THE CENTER AND CHECK IN EACH ITERATION WHICH IS MAX HEIGHT
3.DEFINE AREA (WHICH IS SIMPLE FORMULA LENGHT(lenght from left to right index)*HIEGHT(minimum pointing element))  
4.CHANGE WHEN AREA IS GREATER THAN PREVIOUSLY STORED RESULT
5.CONDITION WHEN LEFT POINTING ELEMENT IS GREATER OR EQUAL TO RIGHT INCREMENT THE POOINTER TO RIGHT (left+=1) || ELSE DECREMENT THE RIGHT POINTER
6.RETURN THE RESULT(result)
"""
        
            