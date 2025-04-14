def productExceptSelf(nums):
    n=len(nums) 
    res=[1]*n
    
    prefix=1
    for i in range(n):
        res[i]=prefix
        prefix *= nums[i]
    
    suffix=1
    for i in range(n-1,-1,-1):
        res[i] *=suffix
        suffix *=nums[i]
    return res



# TIME COMPLEXITY   ->
# SPACE COMPLEXITY  ->


"""
PRODUCT EXCEPT SELF 
## HIGH LEVEL UNDERSTANDING OF THIS CODE :
""ouput = except current product of all""

DEFINE "result" first
so,WE dedecate two loops for PREFIX & SUFFIX 
PREFIX ->starts with one value(1) and in loop it stores product of two forward elements
SUFFIX ->backward loop and product of result[i] current value and nums current value(nums[i])

PSUEDO CODE FOR THIS :
1.DEFINE LIST FOR RESULT WITH ALL ONE VALUE WITH LEN OF GIVEN NUMBER LIST
2.START SUFFIX AND PREFIX WITH VALUE OF ONE
3.LOOP THORUGH ALL PREFIX EXCEPTING THE CURRENT ONE AND APPEND PRODUCT INTO RESULT
4.LOOP THOUGH ALL RESULT FROM BACKWARDS AND APPEND WITH PRODUCT OF CURRENT SUFFIX AND BACKWARD ELEMENT OF NUMBER LIST
5.RETURN THE RESULT 
"""